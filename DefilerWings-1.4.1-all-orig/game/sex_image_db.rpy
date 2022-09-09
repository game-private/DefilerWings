init -1 python hide:
    def label_callback(name, abnormal):
        store.last_label = name
    config.label_callback = label_callback

screen label_callback():
    zorder 10**10
    text "[last_label]" align (0.5, 0) size 25
    
init python:
    import re
    
    """
    Added chain random music function as per Hunters request on Skype:
    """
    def get_random_files(folder, shuffle=True):
        files = [f for f in renpy.list_files() if f.startswith(folder)]

        if shuffle:
            renpy.random.shuffle(files)
            
        return files
    
    """
    Added get random file function as per Hunters request on Skype:
    """
    def get_random_file(folder):
        return renpy.random.choice(get_random_files(folder))
    
    """
    Added by Alex on 07.05.2015
    Instructions to convert into code: https://github.com/OldHuntsman/DefilerWings/issues/51
    """
    class DragonSexImagesDatabase(object):
        def __init__(self):
            self.sex_images = {}
            self.eat_images = set()
                        
            # Первая группа - категория, вторая группа - цвет.
            self.regexp_color = re.compile("img/sex/(.*)/color/(\w+)")
            # Здесь нам нужна только категория. Цвет - any.
            self.regexp_any = re.compile("img/sex/(.*)/any")
                        
            # Получаем список всех файлов в игре из которого фильтруем нужные нам изображения.            
            for file_path in renpy.list_files():
                if file_path.startswith("img/sex"):
                    self.process_sex_image(file_path)
                elif file_path.startswith("img/scene/eat"):
                    self.eat_images.add(file_path)
        
        def process_sex_image(self, file_path):           
            match_color = self.regexp_color.match(file_path)
            if match_color:            
                self.add_sex_image_to_category_and_color(match_color.group(1), match_color.group(2), file_path)
            else:                
                match_any = self.regexp_any.match(file_path)        
        
                if match_any:            
                    self.add_sex_image_to_category_and_color(match_any.group(1), "any", file_path)            
                    
        def add_sex_image_to_category_and_color(self, sex_category, color, file_path):
            if sex_category not in self.sex_images:
                self.sex_images[sex_category] = {}
            
            if color not in self.sex_images[sex_category]:
                self.sex_images[sex_category][color] = []
#                game.narrator(u'%s %s' %(color,file_path))
            self.sex_images[sex_category][color].append(file_path)            
                
        def get_eat_image(self):
            return renpy.random.sample(self.eat_images, 1).pop()
                            
        def has_image_with_color(self, sex_category):
            # По-идее, следует брать не первую голову, а любую из.
            self.avail_colors=[]   # Доступные цвета
            if sex_category == 'mistress' or sex_category == 'dragon':   # Для Госпожи
              for i in xrange(len(game.dragon.heads)):   # Цикл по головам
                if game.dragon.heads[i] in self.sex_images[sex_category]:   # Цвет присутствует
                  self.avail_colors.append(game.dragon.heads[i])
              if len(self.avail_colors)==0:   # Подходящих цветов нет
                return False
              else:
                self.choosen_color=renpy.random.choice(self.avail_colors)
                return self.choosen_color

            else:    # Для всех остальных типов девушек
              for i in xrange(len(game.dragon.heads)):   # Цикл по головам
                dragon_color=game.dragon.heads[i] #+ "("
                hair_color=store.game.girl.hair_color + ")"
                if dragon_color in self.sex_images[sex_category]:   # Цвет присутствует
                  for j in xrange(len(self.sex_images[sex_category][dragon_color])):
                    if hair_color in self.sex_images[sex_category][dragon_color][j]:
                      self.avail_colors.append(self.sex_images[sex_category][dragon_color][j])
              if len(self.avail_colors)==0:   # Подходящих цветов нет
                return False
              else:
                self.choosen_color=renpy.random.choice(self.avail_colors)
#                game.narrator(u"choosen_color %s" % self.choosen_color)
                return self.choosen_color 

                            
        def get_any_image(self, sex_category):
            """
            returns an image from "any" folder randomly.
            Picks color of hair if available.
            """
            images = self.sex_images[sex_category]["any"]
            correct_hair_images = []
            
            # Get a list of images with correct hair colors:
            if sex_category != "dragon": # We do not do this for dragon frecking the mistress images.
                if store.game.girl.hair_color:
                    for i in images:
                        img_name = i.split("/")[-1]
                        if store.game.girl.hair_color in img_name:
                            correct_hair_images.append(i)
                    
            if correct_hair_images:
                return renpy.random.choice(correct_hair_images)
            else:
                return renpy.random.sample(images, 1).pop()
                                
        def __call__(self, sex_category):
#            game.narrator(u"call has_image_with_color %s" % sex_category)
            if sex_category == "mistress" or sex_category == 'dragon': # @ Unique condition: Always get dragon images!
                if self.has_image_with_color(sex_category):
                    return renpy.random.sample(self.sex_images[sex_category][self.choosen_color], 1).pop()
                else:
                    return self.get_any_image(sex_category)        
            elif not self.has_image_with_color(sex_category):
                return self.get_any_image(sex_category)
#            elif renpy.random.randint(0, 2):
#                return self.get_any_image(sex_category)
            else:
#                 game.narrator(u"color %s" % self.choosen_color)
#                return renpy.random.sample(self.sex_images[sex_category][store.game.dragon.color_eng], 1).pop()
#                return renpy.random.sample(self.sex_images[sex_category][self.choosen_color], 1).pop()
                 return self.choosen_color

