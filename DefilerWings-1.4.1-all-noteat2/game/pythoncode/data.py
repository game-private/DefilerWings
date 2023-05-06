#!/usr/bin/env python
# coding=utf-8

import collections
from pythoncode.historical import historical


class Modifier(object):
    """
    Класс разнообразных модификаторов.
    К примеру: даров владычицы, снаряжения рыцарей, заклинаний и.т.д.
    """

    def __init__(self, attack=('base', (0, 0)), protection=('base', (0, 0)), magic=0, fear=0, energy=0):
        self.attack = attack
        self.protection = protection
        self.magic = magic
        self.fear = fear
        self.max_energy = energy

    def __contains__(self, item):
        return item in self.__dict__

    @staticmethod
    def attack_filter(attack):
        return attack


class Container(collections.defaultdict):
    """
    Класс-хранилище разнообразных свойст/модификаторов
    TODO: реверсивный поиск
    """

    def __init__(self, container_id=None, data=None, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)
        self.id = container_id
        if data is not None:

            for key, value in data.items():
                self.add(key, value)

    def add(self, container_id, data):
        """
        :param container_id: Идентификатор свойства/модификатора
        :param data: dict, содержащий парамерты этого свойства/модификатор
        """
        if container_id not in self:
            if type(data) is dict:
                self[container_id] = Container(container_id, data)
            else:
                self[container_id] = data
        else:
            raise Exception("Already in container")

    def sum(self, parameter):
        """
        :param parameter: Значение, по которому нужно суммировать аттрибуты. Суммирование проводится
                          рекурсивно.
        """
        total = 0
        if parameter in self:
            try:
                total += self[parameter]
            except ValueError:
                pass
        for i in self:
            if type(self[i]) == type(self):
                total += self[i].sum(parameter)
        return total

    def list(self, key):
        """
        Рекурсивно возвращает лист значений по ключу
        :param key: Ключ по которому производится поиск
        :return: Список значений
        """
        result = []
        if key in self:
            if type(self[key]) is list:
                result += self[key]
            else:
                result.append(self[key])
        for i in self:
            if type(self[i]) == type(self):
                result += self[i].list(key)
        return result

    def contains(self, key, value=None):
        """
        Возвращает список айдишников, которые содержат заданный ключ и, если указано, значение.
        :param key: Ключ который должен содержать элемент
        :return: список элеметов содержащих ключ, если таких элементов нет, то пустой список
        """
        result = []
        if key in self:
            if value is None:
                result += [self.id]
            else:
                if self[key] == value:
                    result += [self.id]
        for i in self:
            if type(self[i]) == type(self):
                result += self[i].contains(key, value)
        return result

    def select(self, query):
        """
        Возвращает список айдишников которые подходят под условия указанные в query. Нерекурсивно.
        :param query: список кортежей (ключ, значение) которым должен удовлетворять объект поиска
        :return: спискок удовлетворяюищих элементво
        """
        result = []
        for (key, value) in query:
            if key in self and self[key] == value:
                continue
            else:
                break
        else:
            result.append(self.id)
        for i in self:
            if type(self[i]) == type(self):
                result += self[i].select(query)
        return result

    def type(self):
        """
        For test uses
        """
        return type(self)

    def __getattr__(self, name):
        return self[name]

    def __missing__(self, key):
        return None


def get_description_by_count(description_list, count):
    """ 
    :param description_list: словарь, ключ - минимальное целочисленное значение,
    при котором выведется значение с этим ключом.
    Максимальное число, при котором выведется значение - минимальное значение - 1 следующего по размеру ключа
    :param count: число, для которой нужно подобрать описание
    :return: описание для числа count из словаря description_list
    Например, если description_list = {0:'A', 10:'B'}, 
    то при count < 0 результат - None, при count = 0..9 - 'A', а при count >= 10 - 'B'
    """
    count_list = reversed(sorted(description_list.keys()))
    for count_i in count_list:
        if count >= count_i:
            return description_list[count_i]

# Вызываем демона
max_summon=50


# Ящерик
lizardman_names = [
    u"Ррыгх",
    u"Грых",
    u"Хрыгрх",
    u"Хрыргх",
    u"Гырыгх",
    u"Гыргых",
    u"Ыгхр",
    u"Ыгрых",
    u"Ыррыгх",
    u"Гыргх",
    u"Рхыг",
    u"Ргых",
]

#
# Вор
#

thief_first_names = [
    u"Джек",
    u"Гарри",
    u"Cэм",
    u"Алекс",
    u"Бадди",
    u"Бак",
    u"Чак",
    u"Барри",
    u"Барт",
    u"Барри",
    u"Бивис",
    u"Берт",
    u"Билли",
    u"Биф",
    u"Буч",
    u"Брук",
    u"Брэд",
    u"Вилли",
    u"Вуди",
    u"Гейб",
    u"Генри",
    u"Глен",
    u"Грег",
    u"Дакс",
    u"Декстер",
    u"Дэн",
    u"Джет",
    u"Джесси",
    u"Джоб",
    u"Джой",
    u"Джонни",
    u"Джош",
    u"Двайн",
    u"Дюк",
    u"Зак",
    u"Изи",
    u"Кенни",
    u"Кирк",
    u"Клайв",
    u"Клифф",
    u"Клод",
    u"Ларри",
    u"Мэддисон",
    u"Макс",
    u"Маркус",
    u"Марвин",
    u"Марти",
    u"Мэтт",
    u"Нэш",
    u"Ник",
    u"Олли",
    u"Пол",
    u"Рэй",
    u"Рикки",
    u"Скот",
    u"Спайк",
    u"Стив",
    u"Тэд",
    u"Тони",
    u"Трой",
    u"Фил",
    u"Фокс",
    u"Чак",
    u"Шон",
]

thief_last_names = [
    u"Лысый",
    u"Скользкий",
    u"Шустрый",
    u"Хитрый",
    u"Лис",
    u"Прыгун",
    u"Быстроногий",
    u"Шутник",
    u"Шельма",
    u"Заноза",
    u"Вонючка",
    u"Колючка",
    u"Лис",
    u"Тень",
    u"Скрытный",
    u"Тихоня",
    u"Шмыга",
    u"Ловкие Пальцы",
    u"Крадущийся",
    u"Косой",
    u"Шухер",
    u"Загребущий",
    u"Обманщик",
    u"Притворщик",
    u"Верхолаз",
    u"Ползун",
    u"Рифмоплёт",
    u"Бесчестный",
    u"Беспринципный",
    u"Петушок",
    u"Нервный",
    u"Визгун",
    u"Заика",
    u"Рябой",
    u"Сиворылый",
    u"Криволапый",
    u"Косорылый",
    u"Хриплый",
    u"Висельник",
    u"Хамоватый",
    u"Грубиян",
    u"Забияка",
    u"Лизоблюд",
    u"Вертихвост",
    u"Дурной",
    u"Отморозок",
    u"Беспечный",
    u"Змееуст",
    u"Отравитель",
    u"Ухват",
    u"Быстроногий",
    u"Осторожный",
    u"Гнилозубый",
    u"Безубый",
    u"Белоручка",
    u"Красавчик",
    u"Курощуп",
    u"Клаксон",
    u"Котофей",
    u"Чумазик",
    u"Чумазый",
    u"Чертяка",
    u"Каналья",
    u"Сальный",
    u"Матершинник",
    u"Козодой",
    u"Шустрый",
    u"Шипач",
    u"Напильник",
    u"Бабник",
    u"Бычара",
    u"Салага",
    u"Шнур",
    u"Отмычка",
    u"Болторез",
    u"Свинокол",
    u"Ручечник",
    u"Текайка",
    u"Безбашенный",
    u"Сорвиголова",
    u"Головорез",
    u"Марципан",
    u"Сладкоречивый",
    u"Прищур",
    u"Прихлоп",
    u"Совратитель",
    u"Бесстыдник",
]

thief_abilities = Container(
    "thief_abilities",
    {
        "climber": {
            "name": u"Альпинист",
            "description": u"лазает по скалам",
            "avoids": [],
            "provide": ["alpinism"]
        },
        "diver": {
            "name": u"Ныряльщик",
            "description": u"надолго задерживает дыхание",
            "avoids": [],
            "provide": ["swimming"]
        },
        "greedy": {
            "name": u"Жадина",
            "description": u"крадёт больше сокровищ",
            "avoids": [],
            "provide": []
        },
        "mechanic": {
            "name": u"Механик",
            "description": u"легко обходит обычные ловушки",
            "avoids": ["mechanic_traps"],
            "provide": []
        },
        "magicproof": {
            "name": u"Знаток магии",
            "description": u"разряжает магические ловушки",
            "avoids": ["magic_traps", "magic_traps2", "magic_traps3", "magic_traps4"],
            "provide": []
        },
        "poisoner": {
            "name": u"Отравитель",
            "description": u"игнорирует ядовитых стражей",
            "avoids": ["poison_guards"],
            "provide": []
        },
        "assassin": {
            "name": u"Ассасин",
            "description": u"игнорирует обычных стражей",
            "avoids": ["regular_guards"],
            "provide": []
        },
        "night_shadow": {
            "name": u"Ночная тень",
            "description": u"игнорирует элитных стражей",
            "avoids": ["elite_guards"],
            # Это странно, что он может быть пойман обычными стражами
            "provide": []
        },
        "trickster": {
            "name": u"Ловкач",
            "avoids": [],
            "description": u"не имеет шанса разбудить дракона",
            "provide": []
        },
    })

# Контейнер со списком вещей, с помощью которых вор может преодолеть те или иные проблемы
thief_items_provide = Container(
    "thief_items_provide",
    {
        "flight" : ["flying_boots"],
        "alpinism" : ["flying_boots"],
        "fireproof" : ["cooling_amulet"],
        "coldproof" : ["warming_amulet"],
        "swimming" : ["swiming_amulet"]
    })

thief_items = Container(
    "thief_items",
    {
        "plan": {
            "name": u"План ограбления",
            "cursed": False,
            "level": 1,
            "provide": [],
            "avoids": [],
            "description": u"лучше шансы на успех"
        },
        "scheme": {
            "name": u"Схема тайных проходов",
            "cursed": False,
            "provide": [],
            "avoids": [],
            "description": u"игнорирует стены, решетки и двери"
        },
        "sleep_dust": {
            "name": u"Сонный порошок",
            "cursed": False,
            "provide": [],
            "avoids": [],
            "description": u"дракон не проснётся при грабеже"
        },
        "bottomless_sac": {
            "name": u"Бездонный мешок",
            "cursed": False,
            "provide": [],
            "avoids": [],
            "dropable": True,
            "description": u"уносит вдвое больще сокровищ"
        },
        "antidot": {
            "name": u"Антидот",
            "cursed": False,
            "provide": [],
            "description": u"спасает от ядовитых стражей",
            "avoids": ["poison_guards"]
        },
        "enchanted_dagger": {
            "name": u"Зачарованный кинжал",  # Applied
            "dropable": True,
            "cursed": False,
            "provide": [],
            "description": u"эффективен против охранников",
            "avoids": ["regular_guards"]
        },
        "ring_of_invisibility": {
            "name": u"Кольцо Невидимости",  # Applied
            "dropable": True,
            "cursed": False,
            "provide": [],
            "description": u"проходит мимо стража сокровищницы",
            "avoids": ["elite_guards"]
        },
        "flying_boots": {
            "name": u"Летучие сандалии",  # Applied
            "dropable": True,
            "cursed": False,
            "avoids": [],
            "description": u"может летать",
            "provide": ["flight", "alpinism"]
        },
        "cooling_amulet": {
            "name": u"Охлаждающий пояс",  # Applied
            "dropable": True,
            "cursed": False,
            "avoids": [],
            "description": u"защищает от огня",
            "provide": ["fireproof"]
        },
        "warming_amulet": {
            "name": u"Согревающие перчатки",  # Applied
            "dropable": True,
            "cursed": False,
            "avoids": [],
            "description": u"защищает от мороза",
            "provide": ["coldproof"]
        },
        "swiming_amulet": {
            "name": u"Амулет подводного дыхания",  # Applied
            "dropable": True,
            "cursed": False,
            "avoids": [],
            "description": u"позволяет дышать под водой",
            "provide": ["swimming"]
        }
    })

# Одинаковые айдишники вещей спасут от того, что у вора может оказаться норамльная.
thief_items_cursed = Container(
    "thief_items_cursed",
    {
        "plan": {
            "name": u"План ограбления", #u"Плохой план",  # Applied
            "level": -1,
            "cursed": True,
            "provide": [],
            "description": u"лучше шансы на успех", #u"-1 к уровню вора",
            "fails": []
        },
        "scheme": {
            "name": u"Схема тайных проходов",  # Фальшивая схема
            "cursed": True,
            "provide": [],
            "description": u"игнорирует стены, решетки и двери" # C трудом осилит неприступность.
        },
        "sleep_dust": {
            "name": u"Сонный порошок",  # Перцовый порошок
            "cursed": True,
            "provide": [],
            "description": u"дракон не проснётся при грабеже" # Проснётся обязательно!
        },
        "bottomless_sac": {
            "name": u"Бездонный мешок", #u"Дырявый мешок",  # Applied
            "cursed": True,
            "provide": [],
            "description": u"уносит вдвое больще сокровищ", #u"Вор не уносит никаких сокровищ",
            "fails": []
        },
        "antidot": {
            "name": u"Антидот",  # Яд
            "cursed": True,
            "provide": [],
            "description": u"спасает от ядовитых стражей",  # Не спасает
            "fails": ["poison_guards"]
        },
        "enchanted_dagger": {
            "name": u"Зачарованный кинжал",  #u"Проклятый кинжал",  # Applied
            "cursed": True,
            "provide": [],
            "description": u"эффективен против охранников", #u"Автоматический успех обычных стражей",
            "fails": ["regular_guards"]
        },
        "ring_of_invisibility": {
            "name": u"Кольцо Невидимости", #u"Кольцо мерцания",  # Applied
            "cursed": True,
            "provide": [],
            "description": u"проходит мимо стража сокровищницы", #u"Автоматический успех элитных стражей",
            "fails": ["elite_guards"]
        },
        "flying_boots": {
            "name": u"Летучие сандалии",  #u"Ощипанные сандалии",  # Applied
            "cursed": True,
            "provide": [],
            "description": u"может летать", #u"Вор автоматически разбивается насмерть, если идет в логово, требующее полёта",
            "fails": ["flight", "alpinism"],
            "provide": ["flight", "alpinism"]
        },
        "cooling_amulet": {
            "name": u"Охлаждающий пояс", #u"Морозильный амулет",  # Applied
            "cursed": True,
            "provide": [],
            "description": u"защищает от огня", #u"Вор замораживается насмерть, если идет в огненное логово",
            "fails": ["fireproof"],
            "provide": ["fireproof"]
        },
        "warming_amulet": {
            "name": u"Согревающие перчатки", #u"Шашлычный амулет",  # Applied
            "cursed": True,
            "provide": [],
            "description": u"защищает от мороза", #u"Вор зажаривается насмерть, если идет в ледяное логово",
            "fails": ["coldproof"],
            "provide": ["coldproof"]
        },
        "swiming_amulet": {
            "name": u"Амулет подводного дыхания",  # Applied
            "cursed": True,
            "provide": [],
            "description": u"позволяет дышать под водой",
            "fails": ["swimming"],
            "provide": ["swimming"]
        }
    })

thief_titles = [
    u"Мародер",
    u"Грабитель",
    u"Взломшик",
    u"Расхититель гробниц",
    u"Мастер-вор",
    u"Глава гильдии"
]

'''
Вызывает label указанный в value словаря. Если указан list, то вызваются все label'ы указанные в
списке в указанном порядке.
В качестве ключевых параметров передаются:
thief - вор стриггеривший ивент
Дополнительно для "start_trap", "die_trap", "pass_trap", "pass_trap_by_luck", "pass_trap_no_influence", "end_trap":
trap - улучшение, которое стриггерило ивент
Дополнительно для "pass_trap_by_luck":
drain_luck - количество удачи, которое отнято у вора прошедшего эту ловушку.
Дополнительно для "die_item", "receive_item":
item - вещь, которую получил вор
'''
thief_events = {
    "spawn": "lb_event_thief_spawn",
    "lair_unreachable": "lb_event_thief_lair_unreachable",
    "prepare": "lb_event_thief_prepare",
    "prepare_usefull": "lb_event_thief_prepare_usefull",
    "find_useless": "lb_event_thief_find_useless",
    "no_dragon": "lb_event_thief_no_dragon",
    "prepare_useless": "lb_event_thief_prepare_useless",
    "lair_enter": "lb_event_thief_lair_enter",
    "flying_boots_death": "lb_event_thief_alpinism_death",
    "warming_amulet_death": "lb_event_thief_warming_death",
    "swiming_amulet_death": "lb_event_thief_swiming_death",
    "cooling_amulet_death": "lb_event_thief_cooling_death",
    "die_inaccessability": "lb_event_thief_die_inaccessability",
    "start_trap": None,
    "die_trap": "lb_event_thief_die_trap",
    "pass_trap": "lb_event_thief_pass_trap",
    "end_trap": None,
    "receive_no_item": "lb_event_thief_receive_no_item",
    "receive_item": "lb_event_thief_receive_item",
    "steal_items": "lb_event_thief_steal_items",
    "retire": None,
    # @Review: Alex: Added new event:label k/v to fill in the gaps:
    "checking_accessability": "lb_event_thief_checking_accessability",
    "checking_accessability_success": "lb_event_thief_checking_accessability_success",
    "trying_to_avoid_traps_and_guards": "lb_event_thief_trying_to_avoid_traps_and_guards",
    "retreat_and_try_next_year": "lb_event_thief_retreat_and_try_next_year",
    "total_retreat": "lb_event_thief_total_retreat",
    "starting_to_rob_the_lair": "lb_event_thief_starting_to_rob_the_lair",
    "took_an_item": "lb_event_thief_took_an_item",
    "took_an_item_trickster": "lb_event_thief_took_an_item_trickster",
    "took_an_item_dust": "lb_event_thief_took_an_item_dust",
    "wrong_dust": "lb_event_thief_wrong_dust",
    "took_an_item_luck": "lb_event_thief_took_an_item_luck",
    "took_an_item_unluck": "lb_event_thief_took_an_item_unluck",
    "lair_empty": "lb_event_thief_lair_empty",
    "awakened_the_dragon": "lb_event_thief_awakened_dragon"
}

#
# Рыцарь
#

knight_first_names = [
    u"Гавейн",
    u"Ланселот",
    u"Галахад",
    u"Персиваль",
    u"Борс",
    u"Кей",
    u"Мордред",
    u"Гарет",
    u"Уриенс",
    u"Ивейн",
    u"Оуэн",
    u"Бедивер",
    u"Гахерис",
    u"Агравейн",
    u"Алан",
    u"Алистэйр",
    u"Алвен",
    u"Ален",
    u"Анакин",
    u"Арден",
    u"Арман",
    u"Анри",
    u"Арчибальд",
    u"Бардрик",
    u"Бардолф",
    u"Барклай",
    u"Барнабас",
    u"Бенван",
    u"Бартоломью",
    u"Бенджамин",
    u"Бедивир",
    u"Беннет",
    u"Бенедикт",
    u"Бертран",
    u"Блейн",
    u"Блейз",
    u"Болдуин",
    u"Валентайн",
    u"Вирджил",
    u"Вилфорд",
    u"Вейланд",
    u"Габриэль",
    u"Гамильтон",
    u"Гарфилд",
    u"Гилберт",
    u"Гордон",
    u"Тайвин",
    u"Дарнелл",
    u"Дастин",
    u"Дейрилл",
    u"Делберт",
    u"Дензэль",
    u"Джаррет",
    u"Джеральт",
    u"Джейсон",
    u"Диггори",
    u"Дилберт",
    u"Дуглас",
    u"Дейтон",
    u"Иглеберт",
    u"Инграм",
    u"Инесент",
    u"Ирвайн",
    u"Карлайл",
    u"Квентин",
    u"Кертис",
    u"Кингслей",
    u"Кларенс",
    u"Кливленд",
    u"Коннор",
    u"Кристофер",
    u"Криспиан",
    u"Лайонел",
    u"Леопольд",
    u"Линдсей",
    u"Листар",
    u"Лоренс",
    u"Мэйверик",
    u"Максимилиан",
    u"Мельбурн",
    u"Милфорд",
    u"Монтгомери",
    u"Мордикейн",
    u"Найджел",
    u"Николас",
    u"Нордберт",
    u"Нимбус",
    u"Нортон",
    u"Норрис",
    u"Оберон",
    u"Олдред",
    u"Орсон",
    u"Осберт",
    u"Перси",
    u"Рассел",
    u"Редклиф",
    u"Редмунд",
    u"Реджинальд",
    u"Рейнольд",
    u"Рональдь",
    u"Рональд",
    u"Рендалл",
    u"Сбастиан",
    u"Сильвестр",
    u"Стэнли",
    u"Теобальд",
    u"Тимоти",
    u"Тобиас",
    u"Трейвис",
    u"Уилберт",
    u"Уилфред",
    u"Уоренн",
    u"Фабиан",
    u"Фкрдинанд",
    u"Фредкрик",
    u"Френсис",
    u"Хаммонд",
    u"Харрисон",
    u"Чарлтон",
    u"Чедвик",
    u"Шелтон",
    u"Шеридан",
    u"Шерман",
    u"Эдвард",
    u"Юлиан",
]

knight_last_names = [
    u"Озерный",
    u"Славный",
    u"Луговой",
    u"Гордый",
    u"Добрый",
    u"Храбрый",
    u"Отважный",
    u"Верный",
    u"Доблесный",
    u"Сияюший",
    u"Прекрасный",
    u"Красивый",
    u"Сверкающий",
    u"Белый",
    u"Сильный",
    u"Зоркий",
    u"Смелый",
    u"Дубощит",
    u"Терпеливый",
    u"Кроткий",
    u"Искатель",
    u"Ревнитель",
    u"Защитник",
    u"Спаситель",
    u"Благонравный",
    u"Примерный",
    u"Прозорливый",
    u"Вещий",
    u"Мудрый",
    u"Дивный",
    u"Мечтатель",
    u"Избранный",
    u"Благородный",
    u"Благословенный",
    u"Славный",
    u"Невинный",
    u"Целомудренный",
    u"Скромный",
    u"Щедрый",
    u"Бережливый",
    u"Удалой",
    u"Миосердный",
    u"Милостивый",
    u"Сладкозвучный",
    u"Бережливый",
    u"Остроумный",
    u"Безземельный",
    u"Белоликий",
    u"Честный",
]

knight_abilities = Container(
    "knight_abilities",
    {
        "brave": {
            "name": u"Отважный",
            "description": u"не боится дракона, как бы страшен он ни был",
            "provide": [],
            "modifiers": ["fearless"]
        },
        "charmed": {
            "name": u"Зачарованный",
            "description": u"доберётся до любого логова в небесах, на земле и на море",
            "provide": ["swimming", "flight", "alpinism"],
            "modifiers": []
        },
        "liberator": {
            # Implemented at Knight._ability_modifiers
            "name": u"Освободитель",
            "description": u"становится сильнее, если в темнице дракона томятся дамы",
            "provide": [],
            "modifiers": []
        },
        "fiery": {
            "name": u"Вспыльчивый",
            "description": u"усиленная атака",
            "provide": [],
            "modifiers": ['atk_up', 'atk_up']
        },
        "cautious": {
            "name": u"Осторожный",
            "description": u"усиленная защита",
            "provide": [],
            "modifiers": ['def_up', 'def_up']
        }
    }
)

knight_items = Container(
    "knight_items",
    {
        # Нагрудники
        "basic_vest": {
            "id": "basic_vest",
            "name": u"Кольчуга",
            "description": u"стандартная защита",
            "type": "vest",
            "basic": True,
            "provide": [],
            "modifiers": []
        },
        "glittering_vest": {
            "id": "glittering_vest",
            "name": u"Сверкающий доспех",
            "description": u"усиленная защита",
            "type": "vest",
            "basic": False,
            "provide": [],
            "modifiers": ['def_up', 'def_up']
        },
        "gold_vest": {
            "id": "gold_vest",
            "name": u"Золочёный доспех",
            "description": u"отменная защита",
            "type": "vest",
            "basic": False,
            "provide": [],
            "modifiers": ['sdef_up']
        },
        "magic_vest": {
            # Implemented at Knight.enchant_equip
            "id": "magic_vest",
            "name": u"Волшебный доспех",
            "description": u"защита от стихий",
            "type": "vest",
            "basic": False,
            "provide": [],
            "modifiers": []
        },
        # Копья
        "basic_spear": {
            "id": "basic_spear",
            "name": u"Стальная пика",
            "description": u"стандартная атака",
            "type": "spear",
            "basic": True,
            "provide": [],
            "modifiers": []
        },
        "blued_spear": {
            "id": "blued_spear",
            "name": u"Воронёное копьё",
            "description": u"усиленная атака",
            "type": "spear",
            "basic": False,
            "provide": [],
            "modifiers": ['atk_up', 'atk_up']
        },
        "spear_with_scarf": {
            "id": "spear_with_scarf",
            "name": u"Копьё с шарфом дамы",
            "description": u"отменная атака",
            "type": "spear",
            "basic": False,
            "provide": [],
            "modifiers": ['satk_up']
        },
        "dragonslayer_spear": {
            # implemented at Knight._item_modifiers and battle_action
            "id": "dragonslayer_spear",
            "name": u"Копьё-драконобой",  # TODO: implement
            "description": u"бьёт наповал",
            "type": "spear",
            "basic": False,
            "provide": [],
            "modifiers": []
        },
        # Мечи
        "basic_sword": {
            "id": "basic_sword",
            "name": u"Стальной меч",
            "description": u"стандартная атака",
            "type": "sword",
            "basic": True,
            "provide": [],
            "modifiers": []
        },
        "glittering_sword": {
            "id": "glittering_sword",
            "name": u"Сияющий клинок",
            "description": u"усиленная атака",
            "type": "sword",
            "basic": False,
            "provide": [],
            "modifiers": ['atk_up', 'atk_up']
        },
        "lake_woman_sword": {
            "id": "lake_woman_sword",
            "name": u"Клинок озёрной девы",
            "description": u"неотразимая атака",
            "type": "sword",
            "basic": False,
            "provide": [],
            "modifiers": ['satk_up']
        },
        "flameberg_sword": {
            "id": "flameberg_sword",
            "name": u"Пылающий фламберг",
            "description": u"огненная атака",
            "type": "sword",
            "basic": False,
            "provide": [],
            "modifiers": ['sfatk_up', 'sfatk_up']
        },
        "icecracker_sword": {
            "id": "icecracker_sword",
            "name": u"Ледоруб-жидобой",
            "description": u"ледяная атака",
            "type": "sword",
            "basic": False,
            "provide": [],
            "modifiers": ['siatk_up', 'siatk_up']
        },
        "thunderer_sword": {
            "id": "thunderer_sword",
            "name": u"Меч-громобой",
            "description": u"атака молнией",
            "type": "sword",
            "basic": False,
            "provide": [],
            "modifiers": ['slatk_up', 'slatk_up']
        },
        # Щиты
        "basic_shield": {
            "id": "basic_shield",
            "name": u"Геральдический щит",
            "description": u"стандартная защита",
            "type": "shield",
            "provide": [],
            "basic": True,
            "modifiers": []
        },
        "polished_shield": {
            "id": "polished_shield",
            "name": u"Полированный щит",
            "description": u"усиленная защита",
            "type": "shield",
            "provide": [],
            "basic": False,
            "modifiers": ['def_up', 'def_up']
        },
        "mirror_shield": {
            # Implemented at Knight._item_modifiers
            "id": "mirror_shield",
            "name": u"Зерцальный щит",
            "description": u"отражает драконье дыхание",
            "type": "shield",
            "basic": False,
            "provide": [],
            "modifiers": []
        },
        # Кони
        "basic_horse": {
            "id": "basic_horse",
            "name": u"Гнедой конь",
            "description": u"Не дает преимуществ",
            "type": "horse",
            "basic": True,
            "provide": [],
            "modifiers": []
        },
        "white_horse": {
            "id": "white_horse",
            "name": u"Белый конь",
            "description": u"усиленная атака и защита",
            "type": "horse",
            "basic": False,
            "provide": [],
            "modifiers": ['atk_up', 'def_up']
        },
        "pegasus": {
            "id": "pegasus",
            "name": u"Пегас",
            "description": u"способен летать",
            "type": "horse",
            "basic": False,
            "provide": ['alpinism','flight'],
            "modifiers": []
        },
        "firehorse": {
            "id": "firehorse",
            "name": u"Конь-огонь",
            "description": u"прыгает по скалам, неуязим для огня",
            "type": "horse",
            "basic": False,
            "provide": ['alpinism',"fireproof"],
            "modifiers": []
        },
        "sivka": {
            "id": "sivka",
            "name": u"Сивка-Бурка",
            "description": u"прыгает по скалам, неуязвим для холода",
            "type": "horse",
            "basic": False,
            "provide": ['alpinism',"coldproof"],
            "modifiers": [ ]
        },
        "kelpie": {
            "id": "kelpie",
            "name": u"Кельпи",
            "description": u"плавает под водой",
            "type": "horse",
            "basic": False,
            "provide": ['swimming'],
            "modifiers": []
        },
        "griffon": {
            "id": "griffon",
            "name": u"Боевой грифон",
            "description": u"усиленная атака, защита и полёт",
            "type": "horse",
            "basic": False,
            "provide": ['alpinism','flight'],
            "modifiers": ['atk_up', 'def_up']
        },
        # Спутники
        "basic_follower": {
            "id": "basic_follower",
            "name": u"Юный оруженосец",
            "description": u"бесполезный шалопай",
            "type": "follower",
            "basic": True,
            "provide": [],
            "modifiers": []
        },
        "squire": {
            "id": "squire",
            "name": u"Ловкий оруженосец",
            "description": u"карабкается по скалам",
            "type": "follower",
            "basic": False,
            "provide": ['alpinism'],
            "modifiers": ['alpinism']
        },
        "veteran": {
            "id": "veteran",
            "name": u"Закалённый оруженосец",
            "description": u"улучшенная защита",
            "type": "follower",
            "basic": False,
            "provide": [],
            "modifiers": ['sdef_up']
        },
        "pythoness": {
            "id": "pythoness",
            "name": u"Ясновидящая спутница",
            "description": u"знает слабости, улучшенная атака",
            "type": "follower",
            "basic": False,
            "provide": [],
            "modifiers": ['satk_up']
        },
        "thaumaturge": {
            "id": "thaumaturge",
            "name": u"Мудрый наставник",
            "description": u"отменная атака и защита",
            "type": "follower",
            "basic": False,
            "provide": [],
            "modifiers": ['satk_up', 'sdef_up']
        },
    }
)

knight_titles = [
    u"Бедный рыцарь",
    u"Странствующий рыцарь",
    u"Межевой рыцарь",
    u"Благородный рыцарь",
    u"Паладин",
    u"Прекрасный принц"]

knight_events = {
    "spawn": "lb_event_knight_spawn",
    "prepare": None,
    "prepare_usefull": None,
    "prepare_useless": "lb_event_knight_prepare_useless",
    "find_useless": "lb_event_knight_find_useless",
    "refuse_horse": "lb_event_knight_refuse_horse",
    "no_dragon": "lb_event_knight_no_dragon",
    "lair_unreachable": "lb_event_knight_lair_unreachable",
    "no_girls": "lb_event_knight_no_girls",
    "talk_proud": "lb_event_knight_talk_proud",
    "talk_cripple": "lb_event_knight_talk_cripple",
    "talk_blind": "lb_event_knight_talk_blind",
    "talk_ogre": "lb_event_knight_talk_ogre",
    "talk_lust": "lb_event_knight_talk_lust",
    "talk_innocent": "lb_event_knight_talk_innocent",
    "talk_lizardman": "lb_event_knight_talk_lizardman",
    "talk_smuggler": "lb_event_knight_talk_smuggler",
    "go_to_lair": "lb_event_knight_go_to_lair",
    "receive_item": "lb_event_knight_receive_item",
    "challenge_start": "lb_event_knight_challenge_start",   # Должен возвращать True или False
                                                            # True - бой с рыцарем начинается
                                                            # False - нет
    "challenge_end": "lb_event_knight_challenge_end",       # В ивент передается параметр result, содержащий
                                                            # теги исхода битвы дракона с рыцарем
}

#
# Логово
#

lair_types = Container(
    "lair_types",
    {
        "impassable_coomb": {
            "name": u"Буреломный овраг",
            "name_locative": u" в Буреломном овраге",
            "inaccessability": 0
        },
        "impregnable_peak": {
            "name": u"Неприступная вершина",
            "name_locative": u" на Неприступной вершине",
            "inaccessability": 1,
            "require": ["alpinism"],
            'prerequisite': ['wings']
        },
        "solitude_citadel": {
            "name": u"Цитадель одиночества",
            "name_locative": u" в Цитаделе одиночества",
            "inaccessability": 1,
            "require": ["alpinism", "coldproof"],
            'prerequisite': ['wings', 'ice_immunity']
        },
        "vulcano_chasm": {
            "name": u"Вулканическая расселина",
            "name_locative": u" в Вулканической расселине",
            "inaccessability": 1,
            "require": ["alpinism", "fireproof"],
            'prerequisite': ['wings', 'fire_immunity']
        },
        "underwater_grot": {
            "name": u"Подводный грот",
            "name_locative": u" в Подводном гроте",
            "inaccessability": 1,
            "require": ["swimming"],
            'prerequisite': ['swimming']
        },
        "underground_burrow": {
            "name": u"Подземная нора",
            "name_locative": u" в Подземной норе",
            "inaccessability": 1,
            "require": [],
            'prerequisite': ['can_dig']
        },
        "dragon_castle": {
            "name": u"Драконий замок",
            "name_locative": u" в Драконьем замке",
            "inaccessability": 1,
            "require": []
        },
        "castle": {
            "name": u"Старые руины",
            "name_locative": u" в Старых руинах",
            "inaccessability": 1,
            "require": []
        },
        "ogre_den": {
            "name": u"Берлога людоеда",
            "name_locative": u" в Берлоге людоеда",
            "inaccessability": 1,
            "require": []
        },
        "broad_cave": {
            "name": u"Просторная пещера",
            "name_locative": u" в Просторной пещере",
            "inaccessability": 1,
            "require": []
        },
        "tower_ruin": {
            "name": u"Руины башни",
            "name_locative": u" в Руинах башни",
            "inaccessability": 1,
            "provide": ["magic_traps"]
        },
        "monastery_ruin": {
            "name": u"Руины монастыря",
            "name_locative": u" в Руинах монастыря",
            "inaccessability": 2,
            "require": []
        },
        "fortress_ruin": {
            "name": u"Руины каменной крепости",
            "name_locative": u" в Руинах каменной крепости",
            "inaccessability": 2,
            "require": []
        },
        "castle_ruin": {
            "name": u"Руины королевского замка",
            "name_locative": u" в Руинах королевского замка",
            "inaccessability": 2,
            "require": []
        },
        "ice_citadel": {
            "name": u"Ледяная цитадель",
            "name_locative": u" в Ледяной цитадели",
            "inaccessability": 2,
            "require": ["alpinism", "coldproof"]
        },
        "vulcanic_forge": {
            "name": u"Вулканическая кузница",
            "name_locative": u" в Вулканической кузнице",
            "inaccessability": 2,
            "require": ["alpinism", "fireproof"]
        },
        "forest_heart": {
            "name": u"Дупло Великого Древа",
            "name_locative": u" в Дупле Великого Древа",
            "inaccessability": 3,
            "provide": ["magic_traps"]
        },
        "cloud_castle": {
            "name": u"Замок в облаках",
            "name_locative": u" в Облачном замке",
            "inaccessability": 3,
            "require": ["flight"]
        },
        "underwater_mansion": {
            "name": u"Подводные хоромы",
            "name_locative": u" в Подводных хоромах",
            "inaccessability": 2,
            "require": ["swimming"]
        },
        "underground_palaces": {
            "name": u"Подгорные чертоги",
            "name_locative": u" в Подгорных чертогах",
            "inaccessability": 3,
            "require": ["alpinism"],
            "provide": ["mechanic_traps"]
        },
    }
)

lair_upgrades = Container(
    "lair_upgrades",
    {
        "mechanic_traps": {
            "name": u"Механические ловушки",
            "protection": 1,
            "success": {
                "abilities": u'После полутора часов аккуратного копания в механизмах вор обезвреживает механические ловушки.',
                "items": u'Это ошибка!',
                "luck": u'Ворюга в последний момент уклоняется от выскочившего из стены копья. Повезло!',
            },
            "fail": {
                "items": u'Это ошибка!',
                "unluck": u'Незадачливый расхититель сокровищ наступает на нажимную плиту и активирует смертоносную механическую ловушку.',
            },
        },
        "lair_brilliance": {
            "name": u"Украшения для логова",
            "protection": 0,
            "brilliance": 10
        },
        "lair_brilliance_gold": {
            "name": u"Золотые полы для логова",
            "protection": 0,
            "brilliance": 10
        },
        "lair_brilliance_gold_heat": {
            "name": u"Ковровые дорожки на золотые полы",
            "protection": 0,
            "brilliance": 1
        },
        "magic_traps": {
            "name": u"Магические ловушки",
            "protection": 1,
            "success": {
                "abilities": u'Вор закрывает глаза и, полностью положившись на своё чувство магии, крайне медленно и аккуратно преодолевает магическуую ловушку',
                "items": u'Это ошибка!',
                "luck": u'Заметив с самый последний момент взблеск магической ловушки, вор счастливо избегает её и проходит дальше.',
            },
            "fail": {
                "items": u'Это ошибка!',
                "unluck": u'Магическая ловушка распыляет неудачливого вора на атомы. Теперь в воздухе стало больше кислорода, а также водорода, углерода, азота и фосфора!',
            }
        },
        "magic_traps2": {
            "name": u"Магические ловушки 2",
            "inaccessability": 1,
            "protection": 1,
            "success": {
                "abilities": u'Вор закрывает глаза и, полностью положившись на своё чувство магии, крайне медленно и аккуратно преодолевает магическуую ловушку',
                "items": u'Это ошибка!',
                "luck": u'Заметив с самый последний момент взблеск магической ловушки, вор счастливо избегает её и проходит дальше.',
            },
            "fail": {
                "items": u'Это ошибка!',
                "unluck": u'Магическая ловушка (2) распыляет неудачливого вора на атомы. Теперь в воздухе стало больше кислорода, а также водорода, углерода, азота и фосфора!',
            }
        },
        "magic_traps3": {
            "name": u"Магические ловушки 3",
            "protection": 1,
            "inaccessability": 2,
            "success": {
                "abilities": u'Вор закрывает глаза и, полностью положившись на своё чувство магии, крайне медленно и аккуратно преодолевает магическуую ловушку',
                "items": u'Это ошибка!',
                "luck": u'Заметив с самый последний момент взблеск магической ловушки, вор счастливо избегает её и проходит дальше.'
            },
            "fail": {
                "items": u'Это ошибка!',
                "unluck": u'Магическая ловушка (3) распыляет неудачливого вора на атомы. Теперь в воздухе стало больше кислорода, а также водорода, углерода, азота и фосфора!',
            }
        },
        "magic_traps4": {
            "name": u"Магические ловушки 4",
            "protection": 2,
            "inaccessability": 3,
            "success": {
                "abilities": u'Вор закрывает глаза и, полностью положившись на своё чувство магии, плывёт на волнах смутных, но мощных магических потоков',
                "items": u'Это ошибка!',
                "luck": u'Заметив с самый последний момент тонкое дыхание магической ловушки, вор счастливо избегает её и проходит дальше.',
            },
            "fail": {
                "items": u'Это ошибка!',
                "unluck": u'Магическая ловушка (4) пережёвывает вора, унося его обезображенное тело в ад',
            }
        },
        "poison_guards": {
            "name": u"Ядовитые стражи",
            "protection": 1,
            "success": {
                "abilities": u'Ядовитая гадина впивается в лодыжку незванного гостя. Увы, он выработал у себя иммунитете ко стольким ядам, что ему грозит разве что лёгкое недомогание!',
                "items": u'Ядовитая гадина впивается в лодыжку незванного гостя. Вор, мысленно благодаря прекрасную альву, торопливо принимает антидот. Пронесло!',
                "luck": u'Вор пробегает мимо ядовитых тварей настолько быстро, что те не успевают его укусить. Повезло!',
            },
            "fail": {
                "items": u'Ядовитая гадина впивается в лодыжку незванного гостя. Вор, мысленно благодаря свою предусмотрительность, торопливо принимает антидот и валится на землю в жутких конвульсиях. Противоядие оказалось поддельным!',
                "unluck": u'Ядовитая тварь неожиданно напала на вора из темноты и ужалила его. Смерть от токсина медленная и мучительная...',
            }
        },
        "regular_guards": {
            "name": u"Обычные стражи",
            "replaces": "smuggler_guards",  # какое улучшение автоматически заменяет
            "protection": 2,
            "success": {
                "abilities": u'Тихий, как ночная тень, злоумышленник прокрадывается внутрь мимо раззяв-охранников.',
                "items": u'Злоумышленник снимает ключевых охранников, бесшумно перерезав им глотки зачарованным кинжалом.',
                "luck": u'Тщательно изучив режим патрулей, злоумышленник проскальзывает внутрь, пользуясь минутной заминкой стражи. Повезло!',
            },
            "fail": {
                "items": u'Злоумышленник пытается снять ключевых охранников, бесшумно перерезав им глотки зачарованным кинжалом, но его парализует в самый неподходящий момент. Кинжал оказался проклятым!',
                "unluck": u'Охранники замечают вторжение и атакуют вора. Короткая, но ожесточённая схватка оканичвается его смертью.',
            }
        },
        "smuggler_guards": {
            "name": u"Наёмные охранники",
            "cost": 100,
            "protection": 2,
            "success": {
                "abilities": u'Тихий, как ночная тень, злоумышленник прокрадывается внутрь мимо раззяв-охранников.',
                "items": u'Злоумышленник снимает наёмных охранников, бесшумно перерезав им глотки зачарованным кинжалом.',
                "luck": u'Тщательно изучив режим патрулей, злоумышленник проскальзывает внутрь, пользуясь минутной заминкой стражи. Повезло!',
            },
            "fail": {
                "items": u'Злоумышленник пытается снять ключевых охранников, бесшумно перерезав им глотки зачарованным кинжалом, но его парализует в самый неподходящий момент. Кинжал оказался проклятым!',
                "unluck": u'Охранники замечают вторжение и атакуют вора. Короткая, но ожесточённая схватка оканичвается его смертью.',
            }
        },
        "elite_guards": {
            "name": u"Элитные стражи",
            "protection": 3,
            "success": {
                "abilities": u'Цепляясь за крошечные выступы под потолком, вор пробирается мимо элитного стража прямо внутрь сокровищницы!',
                "items": u'Решив, что пора спускать все кулдауны, вор надевает на палец Кольцо Невидимости и проскальзывает внутрь сокровищницы мимо элитного охранника. Иногда десять секунд невидимости раз в сутки бывают абсолютно незаменимы!',
                "luck": u'Исполинское чудовище кружит возле дверей сокровищницы. Его движения абсолютно непредсказуемы. Плюнув на всё, вор бежит вперёд и благополучно пробегает мимо. Повезло!',
            },
            "fail": {
                "items": u'Решив, что пора спускать все кулдауны, вор надевает на палец Кольцо Невидимости и пытается проскальзнуть внутрь сокровищницы мимо элитного охранника. Вот только Кольцо оказывается дешёвой подделкой и отказывает в самый неподходящий момент! Кровожадная тварь разрывает вора на куски и с аппетитом пожирает.',
                "unluck": u'Вор пытается незаметно проскользнуть мимо монстра, охраняющего двери в главный зал, но терпит неудачу. Кровожадная тварь разрывает его на куски и пожирает.',

            }
        },
        "gremlin_fortification": {
            "name": u"Укрепления",
            "inaccessability": 1,
            "protection": 0
        },
        "gremlin_servant": {
            "name": u"Слуги-гремлины",
            "cost": 100,
            "protection": 0
        },
        "servant": {
            "name": u"Слуги",
            "replaces": "gremlin_servant",  # какое улучшение автоматически заменяет
            "protection": 0
        }
    }
)

attack_types = ['base', 'fire', 'ice', 'poison', 'sound', 'lightning']
protection_types = ['base', 'scale', 'shield', 'armor']

#
# Дурная слава
#

reputation_levels = {
    0: 0,
    3: 1,
    6: 2,
    10: 3,
    15: 4,
    21: 5,
    28: 6,
    36: 7,
    45: 8,
    55: 9,
    66: 10,
    78: 11,
    91: 12,
    105: 13,
    120: 14,
    136: 15,
    153: 16,
    171: 17,
    190: 18,
    210: 19,
    231: 20
}

reputation_gain = {
    1: u"Этот поступок люди наверняка заметят.",
    3: u"Дурная слава о ваших поступках разносится по королевству.",
    5: u"Сегодня вы стяжали немалую дурную славу.",
    10: u"Об этом деянии услышат  жители всего королевства. И ужаснутся.",
    25: u"О деянии столь ужасном будут сложены легенды, которые не забудутся и через сотни лет",
    -1: u"Дракон успешно воспользовался своей репутацией и потерял её часть"
}

#
# Дракон
#

# имена
dragon_names = [
    u'Азог',
    u'Ауринг',
    u'Алафис',
    u'Брагнор',
    u'Беливирг',
    u'Бладвинг',
    u'Беоргис',
    u'Буран',
    u'Висерин',
    u'Вазгор',
    u'Балерион',
    u'Мераксес',
    u'Вхагар',
    u'Сиракс',
    u'Тираксес',
    u'Вермакс',
    u'Арракс',
    u'Караксес',
    u'Тандрос',
    u'Мунхайд',
    u'Силвервинг',
    u'Вермитор',
    u'Шиптиф',
    u'Вермитор',
    u'Шрикос',
    u'Моргул',
    u'Урракс',
    u'Дрого',
    u'Рейегаль',
    u'Визерион',
    u'Эссовиус',
    u'Гискар',
    u'Валерион',
    u'Вермитракс',
    u'Архоней',
    u'Дестирион',
    u'Алхафтон',
    u'Торогрим',
    u'Коринстраз',
    u'Ираникус',
    u'Чарис',
    u'Итариус',
    u'Изондр',
    u'Литурган',
    u'Таэрад',
    u'Морфалаз',
    u'Нефариан',
    u'Сеарнокс',
    u'Пион',
    u'Ладон',
    u'Сципион',
    u'Эрихтон',
    u'Горонис',
    u'Горгатрокс',
    u'Артаксеркс',
    u'Айтварас',
    u'Балаур',
    u'Орлангур',
    u'Шадизар',
]

dragon_surnames = [
    u'Яростный',
    u'Могучий',
    u'Ужасный',
    u'Бурерождённый',
    u'Зловещий',
    u'Тёмный',
    u'Жестокий',
    u'Надменный',
    u'Жадный',
    u'Алчный',
    u'Безжалостный',
    u'Беспощадный',
    u'Гордый',
    u'Прожорливый',
    u'Громогласный',
    u'Устрашающий',
    u'Погибельный',
    u'Сварливый',
    u'Великолепный',
    u'Завистливый',
    u'Порочный',
    u'Змееглазый',
    u'Длиннохвостый',
    u'Уродливый',
    u'Шипочешуйный',
    u'Злокозненный',
    u'Осквернитель',
    u'Пожиратель',
    u'Разрыватель',
    u'Роковой',
    u'Смертоносный',
    u'Скрытный',
    u'Кровавый',
    u'Саблеклык',
    u'Искуситель',
    u'Бесстыдный',
    u'Смрадный',
    u'Загребущий',
    u'Срамотряс',
    u'Пронзатель',
    u'Сластолюбивый',
    u'Гневный',
    u'Кишкодёр',
    u'Живодёр',
    u'Живоглот',
    u'Праздный',
    u'Ослизлый',
    u'Разрушитель',
    u'Змееед',
    u'Проклятый',
    u'Кровожадный',
    u'Растлитель',
    u'Безбожный',
    u'Властный',
    u'Лживый',
    u'Буревесник',
    u'Подлый',
    u'Двуличный',
    u'Мудрый',
    u'Зоркий',
    u'Стремительный',
    u'Нечистивый',
]

# Размеры
dragon_size = [
    u'Мелкий',
    u'Средних размеров',
    u'Крупный',
    u'Внушительный',
    u'Огромный',
    u'Исполинский',
]

dragon_size_description = [
    u'Его размеры вряд ли кого-то впечатлят. '
    u'Хотя и сильно вытянутый в длину, змей весит не больше, чем крупная крестьянская собака.',

    u'Он весит примерно столько же, сколько и взрослый, здоровый мужчина. Ничего поразительного.',

    u'Достаточно велик, чтобы поконкурировать размерами с небольшой лошадью или откормленным годовалым бычком.',

    u'В местных лесах вряд ли найдётся зверь, способный потягаться с ним в размерах. '
    u'Разве что самые откормленные быки или пещерные медведи смогут с ним сравниться.',

    u'Пожалуй, по своему весу и размеру он заткнёт за пояс даже мумака из земель к югу и востоку от Султаната. '
    u'Не говоря уже об обитателях лесов и полей этого королевства. Тут ему равных нет.',

    u'На его фоне даже титаны смотрятся бледно, разве что кашалот или кракен весит примерно столько же. '
    u'Но могут ли они быть столь же ловкими и смертносными на суше и в воздухе?',
]

head_description = {
    'black': u'испускает ноздрями ядовитые испарения',
    'blue': u'оснащена жабрами, плавниками и блестящей чешуёй.',
    'bronze': u'способна рыть землю как бронзовый ковш',
    'gold': u'способна видеть невидимое (против воров)',
    'green': u'не имеет особых способностей',
    'iron': u'щетинится стальными пластинами',
    'red': u'изрыгает дымное пламя',
    'shadow': u'повелевает жуткой некромантией',
    'silver': u'украшена гребнем, по которому струятся молнии',
    'white': u'обладает леденящим дыханием'
}

wings_description = [
    u'Он ползает, извиваясь по земле, подобно исполинскому змею.',
    u'Он оснащен могучими крыльями, способными нести его по воздуху.',
    u'У него на спине две пары перепончатых крыл',
    u'Он оснащён тремя парами разноразмерных крыльев, обеспечиваюих невероятную маневренность.'
]

paws_description = [
    u'Он ползает, извиваясь по земле, подобно исполинскому змею.',
    u'Он опирается на пару мощных когтистых лап',
    u'У него четыре когтистые лапы.',
    u'Три пары мощных когтистых лап дают ему невероятную подвижность и устойчивость.'
]

# @fdsc
special_features = ('tough_scale', 'gold_scale', 'poisoned_sting', 'clutches', 'horns', 'fangs', 'ugly', 'uglyVirgin', 'attackPVirgin', 'attackIVirgin', 'attackSVirgin', 'attackFVirgin', 'attackLVirgin', 'defenseVirgin', 'tongue', 'spermtoxicos', 'energy')

special_description = [
    u'Его чешуя крепче, чем закалённая цвергами сталь.',
    u'Его чешуя сияет золотом, привлекая девушек',

    u'На конце его длинного, извивающегося хвоста находится страшное жало, сочащееся несущим погибель ядом.',

    u'Его когти острее бритвы и способны пронзить насквозь даже самые прочные доспехи.',

    u'Величественно изогнутые рога защищают его голову с боков и делают облик дракона ещё более внушительным.',

    u'Его огромные клыки внушают трепет врагу, ибо могут играючи разорвать на части даже самого крупного зверя.',

    u'Он настолько чудовищен в своём уродстве, что не каждый отважится даже взглянуть на него прямо, '
    u'а слабые сердцем бегут от одного лишь его вида.',
    u'Ритуалы над девственницами дали ему уродство',
    u'Ритуалы над девственницами дали ему немного атаки ядом',
    u'Ритуалы над девственницами дали ему немного атаки холодом',
    u'Ритуалы над девственницами дали ему немного атаки рёвом',
    u'Ритуалы над девственницами дали ему немного атаки молниями',
    u'Ритуалы над девственницами дали ему немного атаки огнём',
    u'Ритаулы над соблазнёнными девственницами дали ему немного слабой защиты',
    u'Его длинный шершавый язык обладает особенностью доставлять девушкам сладкое, почти непереносимое, удовольствие',
    u'Увеличенное влечение, уменьшающее ярость при ухаживаниях. Великий осеменитель - никогда не рождаются слабые отродья от сильных женщин',
    u'Дракон делает всё так быстро, что время иногда не успевает проходить мимо него'
]

# @fdsc
special_features_rus = {
    "tough_scale": u"Непробиваемая чешуя ",
    "gold_scale": u"Золотая сияющая чешуя",
    "poisoned_sting": u"Ядовитое жало",
    "clutches": u"Бритвенно острые когти",
    "horns": u"Внушительные рога",
    "fangs": u"Саблезубые клыки",
    "ugly": u"Уродство",
	"attackPVirgin": u"Атака ядом от ритуала",
    "attackIVirgin": u"Атака холодом от ритуала",
    "attackSVirgin": u"Атака рёвом от ритуала",
    "attackLVirgin": u"Атака молниями от ритуала",
    "attackFVirgin": u"Атака огнём от ритуала",
    "uglyVirgin": u"Уродство от ритуала",
    "defenseVirgin": u"Общая слабая защита от ритуала",
    "tongue": u"Сладкий язык",
    'spermtoxicos': u"Спермотоксикоз",
    'energy': u"Энергичный дракон"
}

cunning_description = [
    u'В глазах дракона читается хитрость и коварство. Он владеет запретным колдовством.',

    u'Сверкающие подобно полированному антрациту глаза дракона обладают гипнотической силой. '
    u'Его колдовская мощь велика.',

    u'Взгляд дракона светится нечеловеческим коварством. Сила его колдовских чар просто невероятна.',
]

# TODO: Текстовый модуль с числительными
head_num = [
    u'основная',
    u'вторая',
    u'третья',
    u'четвёртая',
    u'пятая',
    u'шестая',
    u'седьмая',
    u'восьмая',
    u'девятая',
    u'десятая'
]

# описание числа голов
head_count = {
    2: u"двуглавый",
    3: u"трехглавый",
    4: u"четырёхглавый",
    5: u"пятиглавый",
    6: u"шестиглавый",
    7: u"семиглавый",
    8: u"восьмиглавый",
    9: u"многоглавый",
    10: u"многоглавый",
    11: u"многоглавый",
}

# Типы голов(цвета)
dragon_heads = {
    'green': [],
    'red': ['fire_breath', 'fire_immunity'],
    'white': ['ice_breath', 'ice_immunity'],
    'blue': ['swimming','aqua_scale'],
    'black': ['black_power', 'poison_breath'],  # black_power -- +1 атака
    'iron': ['iron_scale', 'sound_breath'],  # iron_scale -- +1 защита
    'bronze': ['bronze_scale', 'can_dig'],  # bronze_scale -- +1 защита
    'silver': ['silver_magic', 'lightning_immunity'],
    'gold': ['gold_magic', 'greedy'],  # greedy -- -2 к шансам вора
    'shadow': ['shadow_magic', 'fear_of_dark'],  # fear_of_dark -- +2 к страху
}

heads_name_rus = {
    'red': u"красный",
    'black': u"чёрный",
    'blue': u"синий",
    'gold': u"золотой",
    'silver': u"серебряный",
    'bronze': u"бронзовый",
    'iron': u"стальной",
    'shadow': u"фантомный",
    'white': u"белый",
    'green': u"зеленый"
}

dragon_gifts = dict()

# Заклинания
spell_list = {
}

spell_unknown = {
    # заговоры -- дают иммунитет к атаке выбранного типа
    'fire_protection': ['fire_immunity'],
    'ice_protection': ['ice_immunity'],
    #'poison_protection': ['poison_immunity'],
    'lightning_protection': ['lightning_immunity'],
    #'sound_protection': ['sound_immunity'],
    # сердца -- дают дыхание нужного типа
    'fire_heart': ['fire_breath'],
    'ice_heart': ['ice_breath'],
    'poison_heart': ['poison_breath'],
    'thunder_heart': ['sound_breath'],
    'lightning_heart': ['lightning_breath'],
    # прочие
    'wings_of_wind': ['wings_of_wind'],
    'aura_of_horror': ['aura_of_horror'],
    'unbreakable_scale': ['virtual_head'],
    'spellbound_trap': ['spellbound_trap'],
    # @fdsc
    # 'spellbound_trap2': ['spellbound_trap2'],
    # 'spellbound_trap3': ['spellbound_trap3'],
    'swimmer_spell': ['swimming'],
    'impregnator': ['impregnator'],
}

spell_description_list = {
    # заговоры -- дают иммунитет к атаке выбранного типа
    'fire_protection': [u'Опасный ритуал полностью защитил его от огня.\n'],
    'ice_protection': [u'Чёткие линии магических формул сделали его невосприимчивым к холоду.\n'],
    #'poison_protection': ['poison_immunity'],
    'lightning_protection': [u'Необузданные магические силы позволили ему буквально купаться в молниях.\n'],
    #'sound_protection': ['sound_immunity'],
    # сердца -- дают дыхание нужного типа
    'fire_heart': [u'Опасный ритуал даровал ему власть над пламенем.\n'],
    'ice_heart': [u'Чёткие линии магических формул позволили ему повелевать хладом.\n'],
    'poison_heart': [u'Запретное колдовство позволило ему выдыхать облака чистого, концентрированного яда.\n'],
    'thunder_heart': [u'Благодаря тайным знаниям он может раскалывать криком скалы.\n'],
    'lightning_heart': [u'Необузданные магические силы окутали его ореолом молний.\n'],
    # прочие
    'wings_of_wind': [u'Странное волшебство позволило ему потягаться в воздухе с самим ветром.\n'],
    'aura_of_horror': [u'Чудовищные обряды воплотили в его облике все страхи демонов Ада.\n'],
    'unbreakable_scale': [u'Точные математические расчёты позволили ему воссоздать достоверныую копию ещё одной головы.\n'],
    'spellbound_trap': [u'Дракон потренировался в магических искусствах, усеяв логово ловушками. Вор не пройдёт!\n'],
    # @fdsc
    'spellbound_trap2': [u'Дракон изрядно потрудился, усеяв логово магическими ловушками\n'],
    'spellbound_trap3': [u'Дракон долго и тщательно снаряжал замаскированные и хитрые магические ловушки\n'],
    'swimmer_spell': [u'Чуждая магия позволила ему дышать под водой.\n'],
    'impregnator': [u'Отвратительное чернокнижие наделило его семя невиданной силой.\n'],
    'witch_spell': [u"Чары таинственной и могущественной ведьмы увеличили магическую мощь дракона.\n"],
    'griffin_meat': [u"Плоть грифона даровала дракону магическую мощь! \n"],
    'boar_meat': [u"Плоть вепря даровала атакам дракона убийственную мощь! \n"],
    'bear_meat': [u"Плоть медведя даровала дракону взвешенную и расчётливую осторожность! \n"],
    'shark_meat': [u"Плоть акулы даровала дракону магическую мощь! \n"],
}

# Русское название для отображения заклинания
spell_list_rus = { 
}

spell_book = {
    # заговоры -- дают иммунитет к атаке выбранного типа
    'fire_protection': u"Защита от огня",
    'ice_protection': u"Защита от холода",
    #'poison_protection': u"Защита от яда",
    'lightning_protection': u"Защита от молнии",
    #'sound_protection': u"Защита от грома",
    # сердца -- дают дыхание нужного типа
    'fire_heart': u"Повелитель пламени",
    'ice_heart': u"Властитель хлада",
    'poison_heart': u"Токсичный лорд",
    'thunder_heart': u"Иерихонский рёв",
    'lightning_heart': u"Сила громовержца",
    # прочие
    'wings_of_wind': u"Крылья ветра",
    'aura_of_horror': u"Аура кошмаров",
    'unbreakable_scale': u"Отрастить фантомную голову",
    'spellbound_trap': u"Волшебные ловушки в логово",
    # @fdsc
    'spellbound_trap2': u"Волшебные ловушки в логово (2)",
    'spellbound_trap3': u"Волшебные ловушки в логово (3)",
    'swimmer_spell': u"Подводное дыхание",
    'impregnator': u"Осеменитель",
}

effects_list = {
    # спецеффекты от еды и других прокачек дракона помимо собственных заклинаний
    'boar_meat': ['atk_up'],
    'bear_meat': ['def_up'],
    'griffin_meat': ['mg_up'],
    'shark_meat': ['mg_up'],
    'witch_spell': ['mg_up'],
}

modifiers = {
    # global
    'fire_immunity': Modifier(),
    'community': Modifier(),
    'poison_immunity': Modifier(),
    'lightning_immunity': Modifier(),
    'ice_immunity': Modifier(),
    'sound_immunity': Modifier(),
    'magic_immunity': Modifier(),

    'flight': Modifier(),
    'alpinism': Modifier(),
    'swimming': Modifier(),

    'atk_up': Modifier(attack=('base', (1, 0))),  # 1 простая атака
    'satk_up': Modifier(attack=('base', (0, 1))),  # 1 верная атака
    'sfatk_up': Modifier(attack=('fire', (0, 1))),  # 1 верная атака огнем
    'sfatk_2up': Modifier(attack=('fire', (0, 2))), # 2 верных атаки огнём
    'siatk_up': Modifier(attack=('ice', (0, 1))),  # 1 верная атака льдом
    'siatk_2up': Modifier(attack=('ice', (0, 2))),  # 2 верных атаки льдом
    'slatk_up': Modifier(attack=('lightning', (0, 1))),  # 1 верная атака молнией  
    'slatk_2up': Modifier(attack=('lightning', (0, 2))),  # 2 верных атаки молнией    
    'def_up': Modifier(protection=('base', (1, 0))),  # 1 защита
    'sdef_up': Modifier(protection=('base', (0, 1))),  # 1 верная защита
    'decapitator': Modifier(),  # Обезглавливатель, при наличии этого модификатора у врага дракон вместо получения урона
                                # сразу теряет одну голову
    # Knight-specific
    'fearless': Modifier(),
    # Dragon-specific
    'can_dig': Modifier(),
    'greedy': Modifier(),
    'virtual_head': Modifier(),
    # @fdsc
    'spellbound_trap': Modifier(),
    'spellbound_trap2': Modifier(),
    'spellbound_trap3': Modifier(),
    'impregnator': Modifier(),
    'tongue': Modifier(),
    'spermtoxicos': Modifier(),
    'energy': Modifier(),
    # Заклинания
    'fire_breath': Modifier(attack=('fire', (0, 1))),
    'ice_breath': Modifier(attack=('ice', (0, 1))),
    'poison_breath': Modifier(attack=('poison', (0, 1))),
    'sound_breath': Modifier(attack=('sound', (0, 1))),
    'lightning_breath': Modifier(attack=('lightning', (0, 1))),
    'black_power': Modifier(attack=('base', (1, 0))),
    'iron_scale': Modifier(protection=('scale', (1, 0))),
    'bronze_scale': Modifier(protection=('scale', (1, 0))),
    'silver_magic': Modifier(magic=1),
    'gold_magic': Modifier(magic=1),
    'shadow_magic': Modifier(magic=1),
    'fear_of_dark': Modifier(fear=2),
    'aura_of_horror': Modifier(fear=1),
    'wings_of_wind': Modifier(energy=1),
    #
    'size': Modifier(attack=('base', (1, 0)), protection=('base', (1, 0)), fear=1),
    'paws': Modifier(attack=('base', (1, 0)), energy=1),
    'wings': Modifier(protection=('base', (1, 0)), energy=1),
    'tough_scale': Modifier(protection=('scale', (0, 1))),
    'gold_scale': Modifier(protection=('base', (-3, 0))),
    'clutches': Modifier(attack=('base', (0, 1))),
    'fangs': Modifier(attack=('base', (2, 0)), fear=1),
    'horns': Modifier(protection=('base', (2, 0)), fear=1),
    'ugly': Modifier(fear=2),
	# @fdsc
	'attackPVirgin': Modifier(attack=('poison',    (1, 0))),
    'attackIVirgin': Modifier(attack=('ice',       (1, 0))),
    'attackSVirgin': Modifier(attack=('sound',     (1, 0))),
    'attackLVirgin': Modifier(attack=('lightning', (1, 0))),
    'attackFVirgin': Modifier(attack=('fire',      (1, 0))),
    'uglyVirgin': Modifier(fear=1),
    'defenseVirgin': Modifier(protection=('base', (1, 0))),
    'poisoned_sting': Modifier(attack=('poison', (1, 1))),
    'cunning': Modifier(magic=1),
    #
    'mg_up': Modifier(magic=1),
    'aqua_scale': Modifier(protection=('base', (1, 0))),
}


def get_modifier(name):
    if name in modifiers:
        return modifiers[name]

    raise NotImplementedError(name)

# логова, картинки
lair_image = {
    'ravine': 'ravine'
}

# Словарь с "достопримечательностями",
# ключ - название этапа,
# значение - кортеж из названия этапа для меню и названия метки, к которой нужно совершить переход
special_places = {
    # лесная пещера с огром
    'enc_ogre': (u"Пещера людоеда", 'lb_enc_fight_ogre'),
    'explore_ogre_den': (u"Исследовать пещеру людоеда", 'lb_enc_explore_ogre_den'),
    'create_ogre_lair': (u"Поселиться в пещере людоеда", 'lb_enc_create_ogre_lair'),
    # йотун
    'jotun_full': (u"Ледяная цитадель", 'lb_jotun'),
    'jotun_empty': (u"Пустой замок в горах", 'lb_jotun_empty'),
    # Ифрит
    'ifrit_full': (u"Вулканическая кузня", 'lb_ifrit'),
    'ifrit_empty': (u"Пустая вулканическая кузня", 'lb_ifrit_empty'),
    # Тритон
    'triton_full': (u"Подводные хоромы", 'lb_triton'),
    'triton_empty': (u"Подводные руины", 'lb_triton_empty'),
    # Титан
    'titan_full': (u"Облачный замок", 'lb_titan'),
    'titan_empty': (u"Разорённый облачный замок", 'lb_titan_empty'),
    # рыцарский манор
    'manor_full': (u"Укреплённая усадьба", 'lb_manor'),
    'manor_empty': (u"Заброшенная усадьба", 'lb_manor_empty'),
    # деревянный замок
    'wooden_fort_full': (u"Деревянный замок", 'lb_wooden_fort'),
    'wooden_fort_empty': (u"Опустевший форт", 'lb_wooden_fort_empty'),
    # монастрыь
    'abbey_full': (u"Укреплённый монастрыь", 'lb_abbey'),
    'abbey_empty': (u"Разорённый монастырь", 'lb_abbey_empty'),
    # каменный замок
    'castle_full': (u"Каменная крепость", 'lb_castle'),
    'castle_empty': (u"Пустая крепость", 'lb_castle_empty'),
    # королевский замок
    'palace_full': (u"Королевский замок", 'lb_palace'),
    'palace_empty': (u"Пустой дворец", 'lb_palace_empty'),
    # зачарованный лес
    'enter_ef': (u"Зачарованный лес", 'lb_enchanted_forest'),
    'dead_grove': (u"Заброшенная роща альвов", 'lb_dead_grove'),
    # задний проход в морию
    'backdor_open': (u"Задний проход", 'lb_backdor'),
    'backdor_sealed': (u"Задний проход", 'lb_backdor_sealed'),
    # мория
    'frontgates_guarded': (u"Врата Подгорного Царства", 'lb_frontgates'),
    'frontgates_open': (u"Разбитые врата", 'lb_dwarf_ruins'),
    # Пещера медведя
    'enc_bear': (u"Пещера медведя", 'lb_bear'),
    # Поляна вепря
    'enc_boar': (u"Поляна вепря", 'lb_boar'),
    # Утёс грифона
    'enc_griffin': (u"Утёс грифона", 'lb_griffin'),
    # Акулий риф
    'enc_shark': (u"Акулий риф", 'lb_shark'),
    # Адамантитовый рудник
    'enc_adamant': (u"Адамантитовый рудник", 'lb_enc_mines_adamantine'),
}

# См. is_quest_complete в game.py
quest_list = (
    {   # только для дебага, не используется
        'min_lvl': 25,  # минимальный уровень дракона для получения квеста
        'max_lvl': 25,  # максимальный уровень дракона для получения квеста
        'text': u"Проживи 5 лет.",  # текст квеста
        'fixed_time': 25,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        # ключевое слово для описания задачи, 'autocomplete' - задача выполняется автоматически
        'task': 'autocomplete',
    },
    {   # Набрать дурной славы (уровень 2)
        'min_lvl': 1,  # минимальный уровень дракона для получения квеста
        'max_lvl': 1,  # максимальный уровень дракона для получения квеста
        # текст квеста, {0} будет заменён на требуемый уровень
        'text': u"Ты уже вырос, пора заняться настоящим делом, сыночек. Там, за пределами моих владений, лежат земли Вольных Народов. Это они унизили меня и изгнали в эти бесплодные пустоши. Ты станешь началом Рода, несущего вольным погибель. \n Давай-ка проверим, на что ты способен, родной. Отправляйся в земли Вольных Народов и стяжай себе дурную славу - пусть о тебе говорят, пусть тебя боятся. Только не лезь на рожон, мы же не хотим, чтобы ты умер, не оставив сыновей, верно? Если видишь, что враг силён - убегай. Бей исподтишка. Рыскай по лесам и полям, убивай одиноких женщин, разоряй стада. Мы увидим, как растёт твоя дурная слава. Когда люди начнут шептаться, возвращайся ко мне, и я подарю тебе сына, который станет сильнее тебя и сможет сделать больше. \n Мой совет - не оставайся спать в Землях Вольных. Когда ты устанешь, то захочешь вздремнуть. И сон твой продлится год, а может быть, и дольше, если надо будет залечивать раны. А пока ты спишь, люди будут охотиться за тобой и твоими сокровищами. Чем больше твоя дурная слава, тем больше внимания ты привлечёшь, а пока что тебе это не нужно. Если успеешь достаточно набедокурить до того как совсем устанешь и захочешь спать, иди лучше сразу сюда. В крайнем случае переночуй в овражке. \n Но если пропадёшь больше, чем на пять лет, я сделаю продолжателем рода другого. ",
        'fixed_time': 5,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        # ключевое слово для описания задачи, 'reputation' - проверяется уровень дурной славы
        'task': 'reputation',
        'fixed_threshold': 1,  # 'fixed_'+ ключевое слово для задания фиксированного требуемого значения
    },
    {   # Породить любое потомство.
        'min_lvl': 2,  # минимальный уровень дракона для получения квеста
        'max_lvl': 2,  # максимальный уровень дракона для получения квеста
        'text': u"Ну вот ты и подрос, родной. Ты сильнее совего папы, но всё же ещё не так могуч, чтобы отомстить за меня - это дело для твоих потомков. А знаешь, что нужно делать, чтобы завести детей? Нет-нет, не со мной, глупыш. Пока что не со мной. Надо проверить, на что ты способен, для продолжения Рода я выберу самого лучшего из выводка. \n   У тебя очень сильное семя, ты сможешь оплодотворить кого захочешь. Но принять и выносить твоего ребёнка смогут не все. Чем больше сил будет у женщины, тем лучше выйдет потомство. Обязательно бери дев, которые ещё не знали мужского прикосновения. Разве что для великанш это не имеет значения, одно отродье они смогут тебе подарить, даже если уже рожали обычных детей до того. Ищи для себя лучшую кровь. Горожанка лучше крестьянки. Благородная дама лучше горожанки. У дев альвов в крови магия - а значит, они дадут отличное потомство. \n   Ты первый в роду, и поэтому тебе рано гоняться за волшебными девами, хватит на первой и крестьянок. Поймай где-нибудь у деревни одну, а лучше нескольких. Оплодотвори их и отпусти на волю, ведь пока ты спишь, в логове за ними некому будет смотреть. Если их не убьют свои же, то через год, когда проснёшься, они породят тварей. Не драконов, конечно, драконов могу породить лишь Я, но всё же это будут монстры, которые попортят людям кровушку. Когда что-нибудь вылупится, возвращайся ко мне, и получишь особую награду!  \n   На всё про всё сроку тебе десять лет. Если не справишься за это время, то назад можешь не возвращаться.",  # текст квеста
        'fixed_time': 10,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'task': 'offspring',  # ключевое слово для описания задачи, 'offspring' - породить потомство
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # 'free_spawn' - потомство, рождённое на воле, 'educated_spawn' - воспитанное потомство
        'task_requirements': (('free_spawn', 'educated_spawn'),)
    },
    {   # Снизить боеспособность королевства.
        'min_lvl': 3,  # минимальный уровень дракона для получения квеста
        'max_lvl': 3,  # максимальный уровень дракона для получения квеста
        'text': u"Сегодня день твоего совершеннолетия. Это значит, что пришла пора и тебе, как до того твоим предкам, отправляться в Земли Вольных народов. Среди всех люди - самые мерзкие. Они многочисленны и организованы. Их королевство огромно. И они уже знают о появлении драконов, а значит, будут защищаться. \n   Когда твоя дурная слава растёт, вслед за ней растёт мобилизация королевства. Они будут увеличивать свою армию, вышлют на дороги патрули. Чем выше мобилизация, тем лучше защищено королевство. Но мы можем помешать людям собраться с силами. Для этого подойдут любые способы: можно разорять деревни, жечь амбары и мельницы. Тогда в стране начнётся разруха и мобилизация упадёт. Можно наводнить королевство отродьями, которые отвлекут войска на себя. А можно просто заплатить разбойникам с одинокого острова, чтобы они начали саботаж. Так или иначе, но ты должен уметь справляться с угрозой. Вот что ты должен сделать: \n   Сначала стяжай дурную славу и ложись спать. Как проснёшься, люди уже будут суетиться. Тогда то и надо будет сделать что-нибудь, чтобы умерить их пыл. Когда мобилизация упадёт, считай что сделал всё что нужно. Можешь возвращаться ко мне за наградой! \n   Сроку дам тебе десять лет. Этого должно быть более чем достаточно для такой простой задачи. ",  # текст квеста
        'fixed_time': 10,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        # ключевое слово для описания задачи, 'poverty' - проверяется уровень понижения мобилизации из-за разрухи
        'task': 'poverty',
        'fixed_threshold': 1,  # 'fixed_'+ ключевое слово для задания фиксированного требуемого значения
    },
    {   # Переселиться в приличное логово, сделать там любое улучшение, завести слуг и охрану.
        # минимальный уровень дракона для получения квеста
        'min_lvl': 4,
        # максимальный уровень дракона для получения квеста
        'max_lvl': 4,
        # текст квеста
        'text': u"Ты уже совсем взрослый, сынок. И ты намного сильнее, чем были первые в твоём Роде, настало время драконам вести себя по-королевски. Я хочу, чтобы ты хорошенько обосновался на Землях Вольных. Тебе понадобится настоящее драконье логово, не какой-нибудь сырой овраг или дыра в земле. Лучше найди хорошую пещеру или отбей у какого-нибудь рыцаря поместье или небольшой замок. Тебе потребуются слуги и охрана. Лучше всего, если тебя будут охранять твои же отродья, но для начала сойдут и наёмники с разбойничьего острова. В качестве слуг можно нанять гремлинов, они будут присматривать за пленницами, пока ты спишь. Тварям, рождённым в твоём логове, ты сможешь приказывать, что делать. Если хочешь насолить людям - отпусти их резвиться на волю. Если нужна охрана или слуги, которые не возьмут с тебя денег, оставь их в логове - там найдётся место для слуг, цепных ядовитых тварей, обычной охраны и элитного защитника сокровищ. Если же твоё логово уже под защитой, отправляй разумных отродий ко мне - они станут дополнением к войску гоблинов и размножатся под моей рукой. \n   Гремлины искусные мастера - обязательно закажи у них ловушки и укрепления для своего нового логова, чтобы ворам было сложнее добраться до сокровищницы. Отнесись к обустройству логова со всем возможным вниманием, ведь менять его дело хлопотное - переселяясь, ты потеряешь всё, что нажил до того, кроме разве что сокровищ. \n   Когда у тебя будет достойное жильё со слугами, охраной, ловушками и укреплениями, позови меня посмотреть. Сроку даю тебе десять лет, если справишься, то станешь продолжателем Рода.\n\nУточнение: технически достаточно иметь:\nлюбую ловушку или фортификацию, в том числе - магическую\nСлуг, в том числе наёмных\nОхрану, в том числе наёмную\nБуреломный овраг не считается логовом - квест в нём не будет выполнен",
        # количество лет на выполнение квеста, не зависящее от уровня дракона
        # 'fixed_time': 10,
        # @fdsc
        'fixed_time': 10,
        # ключевое слово для описания задачи, 'lair' - проверяется тип логова и его улучшений
        'task': 'lair',
        # кортеж с описанием препятствий для выполнения квеста,
        # 'impassable_coomb' - буреломный овраг, квест не выполнится с этим типом логова
        'task_obstruction': ('impassable_coomb',),
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # чтобы потребовать список требований - нужно использовать кортеж внутри кортежа
        # а для вариантов среди списка требований - нужно использовать котреж,
        # который будет внутри кортежа для списка, который уже внутри кортежа
        'task_requirements': (
            ('mechanic_traps', 'magic_traps', 'gremlin_fortification'),
            ('gremlin_servant', 'servant'),
            ('poison_guards', 'regular_guards', 'elite_guards', 'smuggler_guards'),
        )
    },
    {   # Поймать вора или одолеть рыцаря в собственном логове.
        'min_lvl': 5,  # минимальный уровень дракона для получения квеста
        'max_lvl': 5,  # максимальный уровень дракона для получения квеста
        'text': u"В твоём возрасте твой отец отправился в Земли Вольных и устроил там отличное логово. Правда, в деле он его толком так и не проверил. Логово нужно дракону не просто так. Там ты хранишь сокровища и держишь пленниц, вынашивающих твоё потомство. Чем больше твоя дурная слава, тем больше злодеев захочет тебя обидеть. \n   Рыцари будут приезжать, пока ты спишь, будить тебя громкими звуками боевого рога и вызывать на бой. Ну как их за это не убивать? Если же рыцарь тебя одолевает, то можно убежать, но тогда все сокровища и пленницы достанутся ему, а логово будет потеряно навсегда! \n   Воры не так опасны, но они очень раздражают. Слетаются на золото, словно мухи на мёд. Вор будет пытаться проникнуть в сокровищницу, пока ты спишь, и стянуть самые ценные вещи прямо у тебя из под носа! Тут-то и пригодятся охранники, укрепления и ловушки. \n Обустрой себе неприступное логово и проверь его в деле - поймай вора или одолей рыцаря. Тогда я смогу спать спокойно, зная, что мои детки способны сами о себе позаботиться и прожить долгую жизнь в землях наших врагов. \n Четверти века должно хватить, но если справишься быстрее - приходи раньше.\n\nУточнение: нужно убить хотя бы одного вора или рыцаря. Требований к наличию в логове укреплений и ловушек - нет. Чтобы рыцарь пришёл в логово, нужно прославиться, а не просто сидеть и ждать",  # текст квеста
        'fixed_time': 25,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'task': 'event',  # ключевое слово для описания задачи, 'event' - должно произойти какое-то событие
        # кортеж с требованиями, нужно либо 'thief_killer' - поймать вора, либо 'knight_killer' - убить рыцаря
        'task_requirements': (('thief_killer', 'knight_killer'),),
    },
    {   # Набрать дурной славы (уровни 6-11)
        'min_lvl': 6,  # минимальный уровень дракона для получения квеста
        'max_lvl': 11,  # максимальный уровень дракона для получения квеста
        # текст квеста, {0} будет заменён на требуемый уровень
        'text': u"Садись и слушай, дитя моё. Твои беззаботные дни окончены, теперь ты взрослый и будешь сам по себе, один в мире людей. Ты сможешь позаботиться о себе, как и все те твои предки. Если же хочешь стать продолжателем рода, то покажи себя в деле - стяжай дурную славу (не менее {0}) и возвращайся ко мне за наградой. \n   Впрочем, не торопись особо. Времени у нас много, но надо думать о будущем. Золото, которое ты соберёшь и отродья, которых ты отправишь в мою армию, очень пригодятся нам, когда придёт час войны. \n   И да будет имя твоё ночным кошмаром для всех Вольных Народов!",
        'lvlscale_time': 5,  # на что нужно умножить уровень дракона, чтобы получить число лет на выполнение
        # ключевое слово для описания задачи, 'reputation' - проверяется уровень дурной славы
        'task': 'reputation',
        'fixed_threshold': 5,  # задаёт фиксированное значения для задачи
        # число, на которое нужно умножить уровень дракона, чтобы получить необходимый уровень
        'lvlscale_threshold': 1,
    },
    {   # Набрать сокровищ
        'min_lvl': 6,  # минимальный уровень дракона для получения квеста
        'max_lvl': 10,  # максимальный уровень дракона для получения квеста
        # текст квеста, {0} будет заменён на требуемый уровень
        'text': u"Вижу, как горят твои глаза при виде золота и женских форм. Ты стал совсем взрослым, и в тебе окрепли драконьи страсти. Это отлично. Но здесь всё золото принадлежит мне, как и все женские прелести. Если хочешь что-то для себя, милый, отправляйся в земли Вольных Народов. Там достаточно металла и плоти. Иди и возьми! \n   Наша армия растёт, им нужно снаряжение, оружие, продовольствие. Нужно золото. Собери для меня сокровища, которые стоили бы не меньше  {0} фартингов. Если твоё золотое ложе будет достаточно дорогим, я позволю тебе продолжить твой Род, и твои потомки прославят тебя!",
        # @fdsc
        'lvlscale_time': 7,  # на что нужно умножить уровень дракона, чтобы получить число лет на выполнение
        'task': 'wealth',  # ключевое слово для описания задачи, 'wealth' - проверяется стоимость сокровищ
        'fixed_threshold': 10000,  # задаёт фиксированное значения для задачи
        # число, на которое нужно умножить уровень дракона, чтобы получить необходимый уровень
        'lvlscale_threshold': 5000,
    },
    {   # Подарок владычице
        'min_lvl': 6,  # минимальный уровень дракона для получения квеста
        'max_lvl': 12,  # максимальный уровень дракона для получения квеста
        # текст квеста, {0} будет заменён на требуемый уровень
        'text': u"Хочешь меня? Я знаю, знаю. Чем старше ты становишься, тем больше хочешь. Тебя снедает желание продолжить свой род, но это право надо заслужить, сын мой. Женщин, знаешь ли, не всегда похищают и насилуют, со мной этот трюк не пройдёт. Но я буду благосклонна, если ты подаришь мне что-нибудь красивое. И дорогое. Не меньше {0} фартингов, а лучше больше! Уверена, ты сможешь отыскать что-нибудь подходящее в сокровищницах Вольных Народов, или даже соберёшь нужные материалы и сделаешь что-то уникальное, специально для меня. Ведь ты хочешь меня… но пройдут годы, прежде чем сможешь получить. Пусть эта страсть питает тебя, дитя моё. Пусть перерастает в злобу. Я хочу, чтобы Вольные почувствовали твою ярость! Иди и принеси мне подарок, я буду терпелива, я дождусь тебя.\n\nУточнение: заказать украшение можно у ювелира в городе",
        # @fdsc
        'lvlscale_time': 7,  # на что нужно умножить уровень дракона, чтобы получить число лет на выполнение
        'task': 'gift',  # ключевое слово для описания задачи, 'wealth' - проверяется стоимость сокровищ
        # 'fixed_threshold': 1500,
        'fixed_threshold': 1000,
        # число, на которое нужно умножить уровень дракона, чтобы получить необходимый уровень
        # 'lvlscale_threshold': 100,
        'lvlscale_threshold': 1000,
    },
    {   # Породить потомка от великанши.
        'min_lvl': 7,  # минимальный уровень дракона для получения квеста
        'max_lvl': 11,  # максимальный уровень дракона для получения квеста
        'text': u"Поздравляю с совершеннолетием. Ты уже вырос и готов, я вижу, как ты на меня глядишь. Всему своё время. Сначала докажи, что ты настоящий мужчина. Обрюхатить крестьянку много ума не надо, с этим и гоблин справится. Но если ты заведёшь потомство от великанши, это уже достижение. Тогда и я соглашусь, что ты достоин стать продолжателем Рода. \n   Только не забывай пожалуйста, что кроме пушечного мяса нашей армии нужно и золото, чем больше ты соберёшь, тем лучше мы будем готовы к войне. \n   Теперь ступай, сей ужас в землях Вольных Народов!",  # текст квеста
        'fixed_time': 50,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'task': 'offspring',  # ключевое слово для описания задачи, 'offspring' - породить потомство
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них, 'giantess' - потомок от великанши
        'task_requirements': 'giantess',
        # требования для анатомии дракона - список из вариантов, достаточных для выполнения задания
        # каждый вариант - словарь, в котором значение - необходимый модификатор анатомии дракона,
        # а значение - пороговое значение, достаточное для выполнения требования
        'anatomy_required': ({'size': 4}, {'cunning': 1}),
        # наличие этого ключа - задание выполняется только один раз в течение игры,
        # значение - ключ для game.unique, который добавится после выполнения
        'unique': 'giantess'
    },
    {   # Разорить рощу альвов
        'min_lvl': 8,  # минимальный уровень дракона для получения квеста
        'max_lvl': 12,  # максимальный уровень дракона для получения квеста
        'text': u"Ты вырос. Стал таким могучим и большим. Сильнее любого из твоих предков, я ведь помню каждого в твоём роду. Ещё немного, и драконы будут готовы исполнить своё предназначение. Но не ты. Однако для тебя у меня есть испытание, достойное твоего могущества и великолепия. До сих пор мы больше досаждали людям, а они и правда самые мерзкие среди всех. Но есть ещё и другие. В лесах прячутся трусливые альвы, дети богини Дану. Покажи им, на что способны драконы. Найди и уничтожь их священное древо, убей их владык, оскверни их волшебные рощи. Там тебя ждут несметные богатства и прекрасные вечно-юные девы. Но помни, что ни одна из них не сравнится со мной. А меня ты сможешь получить только тогда, когда одолеешь лесной народ. \n   Ступай!",  # текст квеста
        'fixed_time': 75,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'prerequisite': 'giantess',  # ключ для game.unique, который необходим для получения этой задачи
        'task': 'event',  # ключевое слово для описания задачи, 'event' - должно произойти какое-то событие
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # 'ravage_sacred_grove' - разорить рощу альвов
        'task_requirements': 'ravage_sacred_grove',
        # наличие этого ключа - задание выполняется только один раз в течение игры,
        # значение - ключ для game.unique, который добавится после выполнения
        'unique': 'ravage_sacred_grove'
    },
    {   # Устроить логово в подгорном царстве цвергов
        'min_lvl': 9,  # минимальный уровень дракона для получения квеста
        'max_lvl': 12,  # максимальный уровень дракона для получения квеста
        'text': u"Ох, какой же ты большой стал. Сильнее всех прочих, я уверена, что именно ты станешь продолжателем Рода, мой милый. Но, как и всем твоим предкам, сначала тебе придётся доказать, что ты этого достоин. Люди для тебя не угроза. Даже альвы не устоят. Но в Вольных Землях нет большего богатства, чем таят в себе подгорные чертоги цвергов. Наложить на них лапу будет очень и очень не просто, задача как раз для такого могучего змея как ты. Одолей цевргов и устрой своё логово в сокровщнице их короля, и тогда я стану твоей. \n    Ступай. Близок час, когда все Вольные Народы склонятся перед могуществом моих детей.",  # текст квеста
        'fixed_time': 75,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'prerequisite': 'ravage_sacred_grove',  # ключ для game.unique, который необходим для получения этой задачи
        'task': 'lair',  # ключевое слово для описания задачи, 'lair' - проверяется тип логова и его улучшений
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # 'ravage_sacred_grove' - разорить рощу альвов
        'task_requirements': 'underground_palaces',
        # наличие этого ключа - задание выполняется только один раз в течение игры,
        # значение - ключ для game.unique, который добавится после выполнения
        'unique': 'underground_palaces'
    },
    {   # Захватить столицу
        'min_lvl': 13,  # минимальный уровень дракона для получения квеста
        'max_lvl': 20,  # максимальный уровень дракона для получения квеста
        'text': u"Подойди ко мне, сын мой. Каким же большим и сильным ты вырос. Нам нет нужды больше ждать, ты будешь тем, кто отомстит за меня. Ты положишь к моим ногам короны владык Вольных Народов. Исполнишь предназначение, ради которого был создан твой Род. \n   Не торопись, я дам тебе достаточно времени на подготовку. Позаботься о том, чтобы наша армия была в полной готовности, нам нужно много бойцов, и чем разнообразнее они будут, тем лучше. Когда настанет время выступать, помни, что тебе придётся пройти несколько битв, и времени на отдых не будет. В каждой битве у нас будут потери. Большие, если ты останешься в стороне, меньшие, если встанешь на остриё атаки. Если понадобится, один раз я сражусь сама. Когда столица людей падёт, остальные сдадутся сами...",  # текст квеста
        'fixed_time': 1000,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'task': 'event',  # ключевое слово для описания задачи, 'event' - должно произойти какое-то событие
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # 'victory' - заглушка для победы
        'task_requirements': 'victory',
    },
)

# Список всех доступных для дракона событий
dragon_events = (
    'ravage_sacred_grove',  # Добавляется при уничтожении священной рощи альвов
    'thief_killer',  # Убил вора
    'knight_killer',  # Убил рыцаря
)

# Необходимая цена подарка
gift_price = {
    'peasant': {
        'lust': 200,
        'proud': 400,
        'innocent': 800,
    },
    'citizen': {
        'lust': 500,
        'proud': 1000,
        'innocent': 2000,
    },
    'princess': {
        'lust': 1500,
        'proud': 3000,
        'innocent': 6000,
    },
}

# Словарь с набором параметров создания/покупки вещей для упрощения вызова
craft_options = {
    'jeweler_buy': {
        'is_crafting': False, 
        'quality': ['rough', 'common', 'skillfully', 'mastery'], 
        'alignment': ['human'], 
        'base_cost': 0, 
        'price_multiplier': 200,
        'by_dragon': False
    },
    'jeweler_craft': {
        'is_crafting': True, 
        'quality': ['skillfully'], 
        'alignment': ['human'], 
        'base_cost': 200, 
        'price_multiplier': 0,
        'by_dragon': False
    },
    'gremlin': {
        'is_crafting': True, 
        'quality': ['random'], 
        'alignment': ['random'], 
        'base_cost': 100, 
        'price_multiplier': 0,
        'by_dragon': False
    },
    'servant': {
        'is_crafting': True, 
        'quality': ['common'], 
        'alignment': [], 
        'base_cost': 0, 
        'price_multiplier': 0,
        'by_dragon': False
    },
    'dragon': {
        'is_crafting': True, 
        'quality': ['random'],
        'alignment': ['random'],
        'base_cost': 0, 
        'price_multiplier': 0,
        'by_dragon': True
    }
}

# Различный лут
loot = {
    'palace': [
        'taller',
        'taller',
        'taller',
        'taller',
        'dublon',
        'dublon',
        'dublon',
        'dish',
        'dish',
        'goblet',
        'goblet',
        'cup',
        'cup',
        'casket',
        'statue',
        'tabernacle',
        'icon',
        'tome',
        'mirror',
        'band',
        'pendant',
        'broch',
        'gemring',
        'seal',
        'crown',
        'scepter',
        'chain',
        'fibula',
        'silver',
        'gold',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'granate',
        'turmaline',
        'aqua',
        'black_pearl',
        'topaz',
        'saphire',
        'ruby',
        'emerald',
    ],

    'knight': [
        'goblet',
        'statue',
        'tome',
        'band',
        'pendant',
        'ring',
        'gemring',
        'seal',
        'armbrace',
        'chain',
        'fibula',
        'taller',
        'taller',
        'taller',
        'dublon',
        'dublon',
    ],
    
    'jeweler': [
        'taller',
        'taller',
        'dublon',
        'dublon',
        'casket',
        'phallos',
        'band',
        'diadem',
        'tiara',
        'earring',
        'necklace',
        'pendant',
        'ring',
        'broch',
        'gemring',
        'armbrace',
        'legbrace',
        'chain',
        'fibula'
    ],
    
    'smuggler': [
        'silver',
        'gold',
        'mithril',
        'adamantine',
        'jasper',
        'turquoise',
        'jade',
        'malachite',
        'corall',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'crystall',
        'beryll',
        'tigereye',
        'granate',
        'turmaline',
        'aqua',
        'pearl',
        'elven_beryll',
        'black_pearl',
        'topaz',
        'saphire',
        'ruby',
        'emerald',
        'goodruby',
        'goodemerald',
        'star',
        'diamond',
        'black_diamond',
        'rose_diamond',
        'taller',
        'dublon',
        'taller',
        'dublon'
    ],
    
    'klad': [
        'goblet',
        'statue',
        'band',
        'diadem',
        'tiara',
        'earring',
        'necklace',
        'pendant',
        'ring',
        'broch',
        'gemring',
        'seal',
        'armbrace',
        'legbrace',
        'crown',
        'scepter',
        'chain',
        'fibula',
        'silver',
        'gold',
        'mithril',
        'adamantine',
        'jasper',
        'turquoise',
        'jade',
        'malachite',
        'corall',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'crystall',
        'beryll',
        'tigereye',
        'granate',
        'turmaline',
        'aqua',
        'pearl',
        'elven_beryll',
        'black_pearl',
        'topaz',
        'saphire',
        'ruby',
        'emerald',
        'goodruby',
        'goodemerald',
        'star',
        'diamond',
        'black_diamond',
        'rose_diamond',
        'taller',
        'dublon',
        'taller',
        'dublon',
        'taller',
        'dublon',
        'taller',
        'dublon',
        'taller',
        'dublon',
    ],
    
    'coins': [
        'farting',
        'taller',
        'dublon'
    ],

    'church': [
        'goblet',
        'cup',
        'casket',
        'statue',
        'tabernacle',
        'icon',
        'tome',
        'seal',
    ],
    
    'raw_material': [
        'silver',
        'silver',
        'silver',
        'silver',
        'silver',
        'silver',
        'silver',        
        'gold',
        'gold',
        'gold',
        'gold',
        'gold',
        'mithril',
        'adamantine',
        'jasper',
        'turquoise',
        'jade',
        'malachite',
        'corall',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'crystall',
        'beryll',
        'tigereye',
        'granate',
        'turmaline',
        'aqua',
        'pearl',
        'elven_beryll',
        'black_pearl',
        'topaz',
        'saphire',
        'ruby',
        'emerald',
        'goodruby',
        'goodemerald',
        'star',
        'diamond',
        'black_diamond',
        'rose_diamond'
    ],

    'any': [
        'farting',
        'taller',
        'dublon',
        'dish',
        'goblet',
        'cup',
        'casket',
        'statue',
        'tabernacle',
        'icon',
        'tome',
        'mirror',
        'comb',
        'phallos',
        'band',
        'diadem',
        'tiara',
        'earring',
        'necklace',
        'pendant',
        'ring',
        'broch',
        'gemring',
        'seal',
        'armbrace',
        'legbrace',
        'crown',
        'scepter',
        'chain',
        'fibula',
        'silver',
        'gold',
        'mithril',
        'adamantine',
        'jasper',
        'turquoise',
        'jade',
        'malachite',
        'corall',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'crystall',
        'beryll',
        'tigereye',
        'granate',
        'turmaline',
        'aqua',
        'pearl',
        'elven_beryll',
        'black_pearl',
        'topaz',
        'saphire',
        'ruby',
        'emerald',
        'goodruby',
        'goodemerald',
        'star',
        'diamond',
        'black_diamond',
        'rose_diamond'
    ],
}

# список специальных мест людей
human_special_places = [
    'lb_manor_found',
    'lb_wooden_fort_found',
    'lb_abbey_found',
    'lb_castle_found',
    'lb_palace_found',
]

death_reason_explain = {  # Дракон объясняет причину смерти
    "alchemist": [u"Она с контрабандистом связалась, а он потом её алхимику сдал, на опыты!",'contrabandist'],
    "alchemist_blind": [u"Она с контрабандистом связалась, я её за это ослепил, а этот пройдоха потом её алхимику сдал, на опыты!",'contrabandist'],
    "alchemist_cripple": [u"Она с контрабандистом связалась, я её за это искалечил, а этот пройдоха потом её алхимику сдал, на опыты!",'contrabandist'],
    "beheaded": [u"Она с контрабандистом связалась, и я приказал этому пройдохе отрубить ей голову. Приказ он выполнил с превеликим удовольствием!",'contrabandist'],
    "berries": [u"А она там грибы и ягоды собирала, и я её в этом соуе и съел!", 'eat'],
    "blind_cloud": [u"Я её ослепил и выкинул прочь из облачного замка, она и разбилась.", 'blind_escape'],
    "blind_elf": [u"Я её ослепил и выкинул прочь из Дупла Великого Древа, она и погибла в Осквернённом лесу.", 'blind_escape'],
    "blind_fire": [u"Я её ослепил и выкинул прочь, и она в каком-то лавовом озере сварилась.", 'blind_escape'], 
    "blind_fire_fire": [u"Я эту ифритку ослепил и выкинул прочь, а потом её какой-то дэв изнасиловал и сожрал", 'blind_escape'],
    "blind_giant_mountain": [u"Я эту великаншу ослепил и выкинул прочь, а потом она в какую-то пропасть упала", 'blind_escape'],
    "blind_ice": [u"Я её ослепил и выкинул прочь, и она на каком-то леднике замёрзла", 'blind_escape'],
    "blind_ice_ice": [u"Я эту йотуншу ослепил и выкинул прочь, а потом её какой-то йети изнасиловал и сожрал", 'blind_escape'],
    "blind_mermaid_sea": [u"Я эту морскую деву ослепил и выкинул прочь, а потом её какой-то кракен сожрал", 'blind_escape'],
    "blind_mermaid_mountain": [u"Я эту морскую деву ослепил и выкинул прочь, ну она в горах и погибла", 'blind_escape'],
    "blind_mermaid_usual": [u"Я эту морскую деву ослепил и выкинул прочь, ну она потом в ветвях и застряла", 'blind_escape'],
    "blind_mountain": [u"Я её ослепил и выкинул прочь, а она потом в какую-то пропасть соравлась", 'blind_escape'], 
    "blind_sea": [u"Я её ослепил и выкинул прочь, а она потом в море утонула", 'blind_escape'],
    "blind_underground": [u"Я её ослепил и выкинул прочь, а она потом в Подгорных Чертогах заблудилась", 'blind_escape'],
    "blind_usual": [u"Я её ослепил и выкинул прочь, а она по пути домой погибла", 'blind_escape'],
    "bone_desert": [u"Она с контрабандистом связалась, а он потом её работорговцам продал, и она по пути в Султанат в пустыне скончалась",'contrabandist'],
    "burned": [u"А её свои же живьём сожгли",'execution'], 
    "cage": [u"А она в Султанат попала, и там её муж в клетку посадил и голодом заморил",'sultan'], 
    "choked": [u"Она с контрабандистом связалась, и я приказал этому пройдохе её задушить. Приказ он выполнил неспешно, обстоятельно и с превеликим удовольствием!",'contrabandist'], 
    "cloud_usual": [u"А она добиралась домой из Облачного замка и нечаянно разбилась.",'escape'],
    "couple_death": [u"Она с контрабандистом связалась, я об этом пронюхал  и решил обеих убить. Жаль, не  успел - они вдвоём яд выпили.",'contrabandist'],
    "cripple_beheaded": [u"Она с ящериком связалась, я об этом прознал и искалечил. Ну а ящерик её из жалости добил.",'lizardman'], 
    "cripple_die": [u"А я её искалечил, и она из-за недостатка ухода умерла.",'cripple'], 
    "cripple_elf": [u"А я её искалечил и из Дупла Великого Древа выкинул, и сквозь неё трава какая-то проросла.",'cripple'],
    "cripple_fire": [u"А я её искалечил и из логова выкинул, и она на вулканическом плато запеклась.",'cripple'], 
    "cripple_fire_fire": [u"А я эту ифритку искалечил и из логова выкинул, а там её какой-то дэв изнасиловал и сожрал.",'cripple'], 
    "cripple_hunger": [u"А я её искалечил, и она потом от голода сдохла.",'cripple'], 
    "cripple_ice": [u"А я её искалечил и из логова выкинул, и она на леднике замёрзла.",'cripple'], 
    "cripple_ice_ice": [u"А я эту йотуншу искалечил и из логова выкинул, а там её какой-то йети изнасиловал и сожрал.",'cripple'], 
    "cripple_impaled": [u"А её искалечил, а потом её мои слуги над колом подвесили. Зубами она цеплялась долго! ",'cripple'],
    "cripple_ogre": [u"А эту огршу искалечил, а потом её свои же сожрали",'cripple'], 
    "cripple_peak": [u"А я её искалечил и из логова выкинул, и она в высокогорье умерла.",'cripple'], 
    "cripple_pregnant_citizen": [u"А я её искалечил, и её потом родственники-горожане усыпили.",'cripple'], 
    "cripple_pregnant_elf": [u"А я её искалечил, и её потом родственники-альвы усыпили.",'cripple'], 
    "cripple_pregnant_mermaid": [u"А я её искалечил, и её потом родственники-тритоны усыпили.",'cripple'],
    "cripple_pregnant_peasant": [u"А я её искалечил, и её потом родственники-крестьяне усыпили.",'cripple'],
    "cripple_pregnant_princess": [u"А я её искалечил, и её потом родственники-аристократы усыпили.",'cripple'], 
    "couple_sculpture": [u"Она с контрабандистом связалась, я её за это искалечил, заставил их с любовником сексом заниматься, а потом в скульптуру превратил.",'contrabandist'], 
    "cripple_underground": [u"А я её искалечил и из логова выкинул, и в Подгорных чертогах от жажды сдохла.",'cripple'], 
    "cripple_underwater": [u"А я её искалечил и из логова выкинул. В общем, она  утонула.",'cripple'],
    "cripple_underwater_mermaid": [u"А я эту морскую деву искалечил и из логова выкинул, и её водой в глубоком жёлобе раздавило.",'cripple'],
    "cripple_usual": [u"А я её искалечил и из логова выкинул,  и она в том лесу сдохла.",'cripple'], 
    "cripple_unknown": [u"А я её искалечил, и она потом умерла. Как именно - не знаю.",'cripple'],
    "crocodile": [u"А она в Султанат попала, и её хатун крокодилам скормила",'sultan'], 
    "crucify": [u"А она в Султанат попала, и там муж на кресте распял",'sultan'], 
    "defeat": [u"Она с ящериком связалась, я об этом прознал и приказал ему её убить... В общем, сражаться пришлось с обоими.",'lizardman_battle'], 
    "disgust_fish": [u"Её рыцарь пытался вытащить, но она по дороге попала в магическую ловушку и оказалась в желудке гигантской рыбы",'knight'], 
    "disgust_toad": [u"Её рыцарь пытался вытащить, но она по дороге попала в магическую ловушку и оказалась в желудке гигантской жабы",'knight'], 
    "drowned": [u"Она связалась с охранником и не пережила своего возлбленного.",'love'], 
    "eat": [u"А я её съел!", 'eat'],
    "elf_death": [u"А эта альва домой вернулась, а потом с чего решила совершить самоубийство. Её монстры в Тёмном лесу сожрали.", 'suicide'], 
    "elf_mermaid_dead": [u"А эта русалка добиралась домой и застряла в ветвях Осквернённого леса.",'escape'], 
    "elf_usual_dead_1": [u"А она добиралась домой из Осквернённого леса, легла отдохнуть на какой-то поляне, и сквозь её тело трава проросла.",'escape'], 
    "elf_usual_dead_2": [u"А она добиралась домой из Осквернённого леса, но попала в цветки к плотоядным растениям.",'escape'], 
    "elf_usual_dead_3": [u"А она добиралась домой из Осквернённого леса, но оказалась заживо съедена суравьями.",'escape'], 
    "elf_usual_dead_4": [u"А она добиралась домой из Осквернённого леса, но по дороге её заразили проклятые семена, и она сгнила заживво.",'escape'],
    "elf_usual_dead_5": [u"А она добиралась домой из Осквернённого леса, но по дороге её драконорождённый убил.",'escape'],
    "elf_murder": [u"А эта альва домой вернулась, а потом ей так секса захотелось, что она пошла в Тёмный лес, к монстрам. Её там и съели.", 'prostitute'], 
    "execution_elf_1": [u"А эту альву свои же вынудили в Тёмный лес отправиться, и её там гигантский паук сожрал",'execution'],
    "execution_elf_2": [u"А эту альву свои же вынудили в Тёмный лес отправиться, и её там альвоед сожрал",'execution'], 
    "execution_elf_3": [u"А эту альву свои же вынудили в Тёмный лес отправиться, и её там плотоядная плессень растворила.",'execution'], 
    "execution_mermaid_1": [u"А эту русалку свои же на берег выкинули, и она там от жажды умерла.",'execution'],
    "execution_mermaid_2": [u"А эту русалку свои же в глубоководный желоб бросили.",'execution'], 
    "execution_mermaid_3": [u"А эту русалку свои родственники убили.",'execution'], 
    "execution_princess_1": [u"А эту аристократку свои же на кол посадили.",'execution'], 
    "execution_princess_2": [u"А эту аристократку свои же выпотрошили.",'execution'],  
    "execution_princess_3": [u"А эту аристократку свои же на дыбе разорвали.",'execution'], 
    "fire_ice_dead": [u"А эта йотунша добиралась домой, но на вулканическом плато изжарилась.",'escape'],
    "fire_giant_dead_1": [u"А эта великанша добиралась домой, но погибла при извержении вулкана.",'escape'],
    "fire_giant_dead_2": [u"А эта великанша добиралась домой, но погибла в битве с адской гончей.",'escape'], 
    "fire_mermaid_dead": [u"А эта морская дева добиралась домой, но на вулканическом плато изжарилась.",'escape'],
    "fire_usual_dead_1": [u"А она добиралась домой, но на вулканическом плато от жажды скончалась.",'escape'], 
    "fire_usual_dead_2": [u"А она добиралась домой, но на вулканическом плато заживо в гейзере сварилась.",'escape'], 
    "fire_usual_dead_3": [u"А она добиралась домой, но на вулканическом плато сорвалась и в лаву упала.",'escape'], 
    "fire_usual_dead_4": [u"А она добиралась домой, но на вулканическом плато в лавовый поток попала",'escape'], 
    "fire_usual_dead_5": [u"А она добиралась домой, но на вулканическом плато её адская гончая сожрала.",'escape'], 
    "forest_usual_dead_1": [u"А она добиралась домой, но её разбойники изнасиловали и убили.",'escape'], 
    "forest_usual_dead_2": [u"А она добиралась домой, но по пути её волки съели.",'escape'],
    "forest_usual_dead_3": [u"А она добиралась домой, но по пути беладонной отравилась.",'escape'], 
    "forest_usual_dead_4": [u"А она добиралась домой, но по пути в трясине утонула.",'escape'],
    "forest_usual_dead_5": [u"А она добиралась домой, но по пути её ядовитый аспид укусил.",'escape'], 
    "gutted": [u"Она с контрабандистом связалась, и я приказал этому пройдохе её выпотрошить. Приказ он выполнил неспешно, обстоятельно и с превеликим удовольствием!",'contrabandist'], 
    "hunger_death": [u"Она от голода умерла.",'hunger'], 
    "ice_fire_dead": [u"А эта ифритка добиралась домой, но на леднике замёрзла.",'escape'], 
    "ice_giant_dead_1":  [u"А эта великанша добиралась домой, но на леднике в трещину угодила.",'escape'], 
    "ice_giant_dead_2":  [u"А эта великанша добиралась домой, но по пути в битве с йети погибла.",'escape'], 
    "ice_mermaid_dead": [u"А эта морская дева добиралась домой, но по пути на леднике замёрщла.",'escape'], 
    "ice_usual_dead_1": [u"А она добиралась домой, но по пути на леднике замёрзла.",'escape'], 
    "ice_usual_dead_2": [u"А она добиралась домой, но по пути на леднике в трещину свалилась.",'escape'],
    "ice_usual_dead_3": [u"А она добиралась домой, но по пути присела отдохнуть, и её снегопад занёс.",'escape'], 
    "ice_usual_dead_4": [u"А она добиралась домой, но по пути под лавину угодила",'escape'], 
    "ice_usual_dead_5": [u"А она добиралась домой, но по пути её йети изнасиловал и сожрал.",'escape'],
    "kitchen_boil": [u"Её слуги сварили и съели.",'kitchen'], 
    "kitchen_fry": [u"Её слуги на противине зажарили и съели.",'kitchen'],
    "kitchen_spit": [u"Её слуги насадили на вертел, зажарили и съели.",'kitchen'], 
    "knight_beheaded":  [u"Она с рыцарем сбежала, но потом он по её просьбе отрубил ей голову.",'suicide'], 
    "knight_beheaded_rage": [u"Она получила от меня подарок и заявила рыцарю, что дракон её любит. Ну он ей голову и отсёк.",'knight_beheaded'], 
    "lair_birth": [u"Она в логове умерла, при родах.",'birth'], 
    "mermaid_death": [u"А эта русалка благополучно домой вернулась, а потом с чего-то решила совершить самоубийство. Её акула сожрали.", 'suicide'], 
    "mermaid_murder": [u"А эта русалка благополучно домой вернулась, а потом ей так секса захотелось, что она стала путников соблазнять и в глубины утаскивать. Ну и однажды нарвалась на бандитов, которые её и убили.", 'prostitute'],
    "peak_giant_dead": [u"А эта великанша добиралась домой, но в горах в пропасть упала.",'escape'],
    "peak_mermaid_dead": [u"А эта русалка добиралась домой, но по пути в горах погибла.",'escape'], 
    "peak_usual_dead_1": [u"А она добиралась домой, но в горах сломала  ногу и так никуда и не дошла.",'escape'], 
    "peak_usual_dead_2": [u"А она добиралась домой, но в горах оступилась и сорвалась в пропасть.",'escape'], 
    "peak_usual_dead_3": [u"А она добиралась домой, но в горах повисла на карнизе, да так и не смогла подтянуться.",'escape'], 
    "peak_usual_dead_4": [u"А она добиралась домой, но в горах попала под камнепад.",'escape'], 
    "peak_usual_dead_5": [u"А она добиралась домой, но в горах её гоблины изнасиловали и съели.",'escape'], 
    "peril": [u"А она в Султанат попала, и её хатун убила, перетянув живот верёвкой.",'sultan'],
    "poison": [u"А она в Султанат попала, и её хатун отравила.",'sultan'], 
    "princess_death": [u"А эта аристократка благополучно домой вернулась, а потом с чего-то решила совершить самоубийство. Она живот себе разрезала.", 'suicide'],
    "princess_murder": [u"А эта аристократка благополучно домой вернулась, а потом ей так секса захотелось, что она стала весьма и весьма неразборчивой. Ну и попала на ритуал к демонопоклонникам.", 'prostitute'],
    "rape_army": [u"Она с ящериком связалась и вместе с ним к Тёмной Госпоже сбежала, а там ящерик погиб, и её затрахали до смерти.",'lizardman'],
    "rape_death": [u"Нуу... она почему-то моих ухаживаний не вынесла. И скончалась.",'rape_death'], 
    "rape_goblin": [u"Она с ящериком связалась и вместе с ним к Тёмной Госпоже сбежала, ну а там её гоблины затрахали до смерти.",'lizardman'],
    "rape_troll": [u"Она с ящериком связалась и вместе с ним к Тёмной Госпоже сбежала, ну а там её тролли затрахали до смерти.",'lizardman'],
    "sands": [u"А она в Султанат попала, и её хатун в зыбучих песках утопила.",'sultan'], 
    "scorpion": [u"А она в Султанат попала, и там муж её скорпионами затравил.",'sultan'], 
    "suicide_sucsess_cloud": [u"Она покончила с собой, выпрыгнув из Облачного замка.",'suicide_prison'], 
    "suicide_sucsess_elf": [u"Она покончила с собой, оставшись на ночь на полянке с живой травой.",'suicide_prison'], 
    "suicide_sucsess_fire": [u"Она покончила с собой, умерев от теплового удара в вулканическом логове.",'suicide_prison'],
    "suicide_sucsess_ice": [u"Она покончила с собой, замёрзнув в ледяном логове.",'suicide_prison'], 
    "suicide_sucsess_sea": [u"Она покончила с собой, утопившись в водном логове.",'suicide_prison'], 
    "suicide_sucsess_undeground": [u"Она покончила с собой, закупорив себя в герметичном чертоге.",'suicide_prison'], 
    "tiger": [u"А она в Султанат попала, и там муж её тиграм скормил.",'sultan'], 
    "trap_drown": [u"Её рыцарь пытался вытащить, но она по дороге попала в ловушку и утонула",'knight'], 
    "trap_pendulum": [u"Её рыцарь пытался вытащить, но она по дороге попала в ловушку, и её маятник надвое рассёк.",'knight'], 
    "trap_thorns": [u"Её рыцарь пытался вытащить, но она по дороге попала в ловушку, и её плита с шипами задавила.",'knight'], 
    "turned_apart": [u"А я решил посмотреть, что у неё внутри, и на части её разорвал!",'turned_apart'], 
    "underground_mermaid_dead": [u"А эта русалка добиралась домой, но по пути в Подгорных чертогах погибла.",'escape'], 
    "underground_usual_dead_1": [u"А она добиралась домой, но заблудилась в Подгорных чертогах.",'escape'], 
    "underground_usual_dead_2": [u"А она добиралась домой, но утонула в подземном озере.",'escape'],
    "underground_usual_dead_3": [u"А она добиралась домой, но в какой-то пещере упала в бездонный колодец.",'escape'],
    "underground_usual_dead_4": [u"А она добиралась домой, но в какой-то пещере застряла намертво. В обоих смыслах слова.",'escape'], 
    "underground_usual_dead_5": [u"А она добиралась домой, но при выходе из Подгорных чертогов её гоблины изнасиловали и съели.",'escape'], 
    "underwater_fire_dead": [u"А эта ифритка добиралась домой, но не сумела доплыть до берега.",'escape'],  
    "underwater_giant_dead_1": [u"А эта великанша добиралась домой, но не сумела доплыть до берега.",'escape'],  
    "underwater_giant_dead_2": [u"А эта великанша добиралась домой, но погибла в битве с кракеном.",'escape'], 
    "underwater_mermaid_dead": [u"А эта русалка добиралась домой, но по пути погибла в битве с кракеном.",'escape'], 
    "underwater_usual_dead_1": [u"А она добиралась домой, но не сумела доплыть до берега из-за неожиданной судороги.",'escape'],
    "underwater_usual_dead_2": [u"А она добиралась домой, но так как плавать не умела, то далеко и не уплыла.",'escape'], 
    "underwater_usual_dead_3": [u"А она добиралась домой, но не сумела доплыть до берега - угодила в мощное встречное течение.",'escape'], 
    "underwater_usual_dead_4": [u"А она добиралась домой, но не сумела доплыть до берега - её шторм в открытом море застиг.",'escape'],
    "underwater_usual_dead_5": [u"А она добиралась домой, но не сумела доплыть до берега - погибла в битве с гигантским кракеном.",'escape'],
}

death_reason_desc = {  # Описание причин смерти
    "alchemist": u"Замученные безумными алхимиками:",
    "alchemist_blind": u"Слепые, замученные безумными алхимиками:",
    "alchemist_cripple": u"Калеки, замученные безумными алхимиками:",
    "beheaded": u"Убитые отрезанием головы контрабандистом:",
    "berries": u"Крестьянки в соусе, съеденные драконом:",
    "blind_cloud": u"Слепые, выброшенные из облачного замка:",
    "blind_elf": u"Слепые, погибшие в осквернённом лесу:",
    "blind_fire": u"Слепые, упавшие в лавовое озеро:",
    "blind_fire_fire": u"Слепые ифритки, изнасилованные и съеденные дэвами:",
    "blind_giant_mountain": u"Слепые великанши, сорвавшиеся в пропасть:",
    "blind_ice": u"Слепые, замёрзшие на горных ледниках:",
    "blind_ice_ice": u"Слепые йотунши, изнасилованные и съеденные йети:",
    "blind_mermaid_sea": u"Слепые морские девы, съеденные кракеном:",
    "blind_mermaid_mountain": u"Слепые морские девы, погибшие на высокогорье:",
    "blind_mermaid_usual": u"Слепые морские девы, застрявшие в ветвях:",
    "blind_mountain": u"Слепые, сорвавшиеся в пропасть:",
    "blind_sea": u"Слепые, утонувшие в море:",
    "blind_underground": u"Слепые, заблудившиеся в Подгорных чертогах:",
    "blind_usual": u"Слепые, погибшие по пути домой:",
    "bone_desert": u"Погибшие в пустыне по пути в Султанат:",
    "burned": u"Горожанки, сожжённые живьём:",
    "cage": u"Заморенные голодом в клетке мужем из Султаната:",
    "cannibal": u"Съеденные собственным отцом в голодный год:",
    "choked": u"Задушенные контрабандистом:",
    "cloud_usual": u"Разбившиеся при падении из облачного замка:",
    "couple_death": u"Принявшие яд вместе с возлюбленным-контрабандистом:",
    "cripple_beheaded": u"Калеки, убитые ящериками из милосердия:",
    "cripple_die": u"Калеки, умершие из-за недостаточного ухода:",
    "cripple_elf": u"Калеки, убитые травой, проросшей сквозь тело:",
    "cripple_fire": u"Калеки, запёкшиеся на вулканическом плато:",
    "cripple_fire_fire": u"Искалеченные ифритки, изнасилованные и съеденные дэвами:",
    "cripple_hunger": u"Калеки, скончавшиеся от голода:",
    "cripple_ice": u"Калеки, замёрзшие на горном леднике:",
    "cripple_ice_ice": u"Искалеченные йотунши, изнасилованные и съеденные йети:",
    "cripple_impaled": u"Калеки, участвовашие в финальном аттракционе драконьих слуг:",
    "cripple_ogre": u"Калеки-огрши, съеденные своими сородичами:",
    "cripple_peak": u"Калеки, нашедшие вечный покой в высокогорье:",
    "cripple_pregnant_citizen": u"Калеки-горожанки, усыплённые родственниками из опасений и жалости:",
    "cripple_pregnant_elf": u"Калеки-альвы, усыплённые из-за нарушения природного равновесия:",
    "cripple_pregnant_mermaid": u"Калеки-русалки, усыплённые родственниками из опасений и жалости:",
    "cripple_pregnant_peasant": u"Калеки-крестьянки, усыплённые родственниками из нищеты:",
    "cripple_pregnant_princess": u"Калеки-аристократки, усыплённые родственниками из-за возможного урона чести рода:",
    "couple_sculpture": u"Калеки, ставшие вечной скульптурой в прозрачной смоле:",
    "cripple_underground": u"Калеки, скончавшиеся от жажды в Подгорных чертогах:",
    "cripple_underwater": u"Калеки, утонувшие в море:",
    "cripple_underwater_mermaid": u"Искалеченные морские девы, раздавленные водой в глбоководном желобе:",
    "cripple_usual": u"Калеки, нашедшие вечный покой в глухом лесу:",
    "cripple_unknown": u"Калеки, подробности смерти которых неизвестны:",
    "crocodile": u"Скормленные крокодилам по приказу хатун:",
    "crucify": u"Распятые на кресте мужем из Султаната:",
    "deAd_bdsm_death": u"Рыжие ведьмы, запытанные насмерть:",
    "deAd_elf_burned": u"Коварные альвы, сожжённые рыжими ведьмами:",
    "deAd_elf_dead": u"Коварные альвы, прогневавшие дракона:",
    "deAd_elf_fail": u"Коварные альвы, погибшие в поединке с драконом:",
    "deAd_elf_lie": u"Коварные альвы, убитые пождозрительным драконом:",
    "deAd_elf_loose": u"Коварные альвы, погибшие в поединке с Тёмной сестрой:",
    "deAd_fire_witch": u"Рыжие ведьмы, ставшие воплощением огня:",
    "deAd_kind_eat": u"Рыжие ведьмы, съеденные драконом:",
    "deAd_murder": u"Рыжие ведьмы, задушенные коварными альвами:",
    "deAd_zombie": u"Рыжие ведьмы, изнасилованные и убитые зомби и вставшие в их ряды:",
    "defeat": u"Убитые в поединке с драконом вместе с возлюбленным-ящериком:",
    "disgust_fish": u"Переваренные гигантской рыбой:",
    "disgust_toad": u"Переваренные гигантской лягушкой:",
    "drowned": u"Утопившиеся из-за убийства возлюбленного рыцарем:",
    "eat": u"Съеденные драконом:",
    "eat_architot": u"Фрейлины, съеденные драконом во время битвы с Архитотом:",
    "elf_death": u"Отчаявшиеся альвы, съеденые монстрами:",
    "elf_mermaid_dead": u"Русалки, застрявшие на ветвях в осквернённом лесу:",
    "elf_usual_dead_1": u"Убитые травой, проросшей сквозь тело:",
    "elf_usual_dead_2": u"Заживо съеденные плотоядными растениями:",
    "elf_usual_dead_3": u"Заживо съеденные муравьями:",
    "elf_usual_dead_4": u"Заражённые проклятыми семенами и сгнившие заживо:",
    "elf_usual_dead_5": u"Убитые драконорожденными:",
    "elf_murder": u"Развращённые альвы, изнасилованые и съеденные монстрами:",
    "execution_elf_1": u"Альвы, съеденные гигантским пауком:",
    "execution_elf_2": u"Альвы, съеденные альвоедом:",
    "execution_elf_3": u"Альвы, съеденные плотоядной плесенью:",
    "execution_mermaid_1": u"Русалки, уумершие на берегу от жажды:",
    "execution_mermaid_2": u"Русалки, утопленные в глубоководном желобе:",
    "execution_mermaid_3": u"Русалки, убитые родичами:",
    "execution_peasant_1": u"Крестьянки, растерзанные сородичами:",
    "execution_peasant_2": u"Утопленные крестьянки:",
    "execution_peasant_3": u"Крестьянки, закопанные живьём:",
    "execution_princess_1": u"Аристократки, прилюдно посаженные на кол:",
    "execution_princess_2": u"Аристократки, казнённые через вскрытие живота:",
    "execution_princess_3": u"Аристократки, прилюдно разорванные на дыбе:",
    "fire_ice_dead": u"Йотунши, погибшие от жара на вулканическом плато:",
    "fire_giant_dead_1": u"Великанши, погибшие при извержении вулкана:",
    "fire_giant_dead_2": u"Великанши, погибшие в битве с адской гончей:",
    "fire_mermaid_dead": u"Морские девы, погибшие от жара на вулканическом плато:",
    "fire_usual_dead_1": u"Умершие от жажды на вулканическом плато:",
    "fire_usual_dead_2": u"Заживо сварившиеся в гейзере:",
    "fire_usual_dead_3": u"Сорвавшиеся и упавшие в лаву:",
    "fire_usual_dead_4": u"Попавшие в лавовый поток:",
    "fire_usual_dead_5": u"Съеденные адской гончей:",
    "free_birth": u"Умершие при родах на воле:",
    "forest_queen_innocent": u"Королевы альвов, покончившие с собой, чтобы не достаться дракону:",
    "forest_queen_proud": u"Королевы альвов, убившие себя темнейшим колдовством ради мести дракону:",
    "forest_usual_dead_1": u"Изнасилованные и убитые разбойниками:",
    "forest_usual_dead_2": u"Съеденные волками:",
    "forest_usual_dead_3": u"Отравившиеся беладонной:",
    "forest_usual_dead_4": u"Утонувшие в трясине:",
    "forest_usual_dead_5": u"Укушенные ядовитым аспидом:",
    "gutted": u"Убитые вытягиванием кишок контрабандистом:",
    "hanged": u"Прилюдно повешенные горожанки:",
    "hanged_self_citizen": u"Горажанки, повесившиеся от отчаяния:",
    "hunger_death": u"Умершие от голода:",
    "ice_fire_dead": u"Ифритки, замёрзие на леднике:",
    "ice_giant_dead_1": u"Великанши, свалившиеся в гигантскую трещину на леднике:",
    "ice_giant_dead_2": u"Великанши, погибшие в битве с йети:",
    "ice_mermaid_dead": u"Морские девы, замёрзие на леднике:",
    "ice_usual_dead_1": u"Замёрзшие насмерть:",
    "ice_usual_dead_2": u"Упавшие в трещину на леднике:",
    "ice_usual_dead_3": u"Занесённые снегопадом:",
    "ice_usual_dead_4": u"Попавшие под лавину:",
    "ice_usual_dead_5": u"Изнасилованные и съеденные йети:",
    "kitchen_boil": u"Сваренные и съеденные слугами:",
    "kitchen_fry": u"Зажаренные на противине и съеденные слугами:",
    "kitchen_spit": u"Насаженные на вертел и съеденные слугами:",
    "knight_beheaded": u"Обезглавленные рыцарем по своей собственной просьбе:",
    "knight_beheaded_rage": u"Обезглавленные рыцарем в припадке ярости:",
    "lair_birth": u"Умершие при родах в логове:",
    "maniac": u"Горожанки, убитые маньяками:",
    "mermaid_death": u"Русалки, съеденные акулами:",
    "mermaid_murder": u"Развращённые русалки, убитые бандитами:",
    "peak_giant_dead": u"Великанши, упавшие в пропасть на высокогорье:",
    "peak_mermaid_dead": u"Морские девы, погибшие на высокогорье:",
    "peak_usual_dead_1": u"Сломавшие ногу на высокогорье:",
    "peak_usual_dead_2": u"Оступившиеся и сорвавшиеся в пропасть:",
    "peak_usual_dead_3": u"Не смогшие подтянуться и сорвавшиеся в пропасть:",
    "peak_usual_dead_4": u"Попавшие под камнепад:",
    "peak_usual_dead_5": u"Съеденные гоблинами на высокогорье:",
    "peasant_death": u"Повесившиеся крестьянки:",
    "peasant_murder": u"Крестьянки, связавшиеся с бандитами и оставленные на поживу воронам:",
    "peril": u"Убитые перетягиванием живота по приказу хатун:",
    "poison": u"Отравленные хатун:",
    "princess_death": u"Аристократки, совершившие харакири:",
    "princess_murder": u"Аристократки, принесённые в жертву демонопоклонниками:",
    "rape_army": u"Погибшие в армии Тёмной Госпожи из-за проигрыша любовника-ящерика:",
    "rape_death": u"Не вынесшие ухаживаний дракона:",
    "rape_goblin": u"Насмерть изнасилованные гоблинами при устройстве в армию Тёмной Госпожи:",
    "rape_troll": u"Насмерть изнасилованные троллями при устройстве в армию Тёмной Госпожи:",
    "sands": u"Утопленные в зыбучих песках по приказу хатун:",
    "scorpion": u"Затравленные скорпионами мужем из Султаната:",
    "suicide_sucsess_cloud": u"Суицидницы, спрыгнувшие с облачного замка:",
    "suicide_sucsess_elf": u"Суицидницы, лёгшие на полянку с живой травой:",
    "suicide_sucsess_fire": u"Суицидницы, погибшие от жара в огненном чертоге:",
    "suicide_sucsess_ice": u"Суицидницы, погибшие от холода в ледяной комнате:",
    "suicide_sucsess_sea": u"Суицидницы, утопившиеся в мелком бассейне:",
    "suicide_sucsess_undeground": u"Суицидницы, уморившие себя в герметичном чартоге:",
    "tiger": u"Скормленные тиграм мужем из Султаната:",
    "trap_drown": u"Беглянки, угодившие в ловушку и утонувшие:",
    "trap_pendulum": u"Беглянки, угодившие в ловушку и рассечённые маятником на две части:",
    "trap_thorns": u"Беглянки, угодившие в ловушку и задавленные плитой с шипами:",
    "turned_apart": u"Разорванные драконом на части из чистой забавы:",
    "underground_mermaid_dead": u"Морские девы, погибшие в Подгорных чертогах:",
    "underground_usual_dead_1": u"Заблудившиеся в Подгорных чертогах:",
    "underground_usual_dead_2": u"Утонувшие в подземном озере:",
    "underground_usual_dead_3": u"Упавшие в бездонный колодец:",
    "underground_usual_dead_4": u"Застрявшие в пещере у самой поверхности:",
    "underground_usual_dead_5": u"Съеденные гоблинами при выходе из Подгорных чертогов:",
    "underwater_fire_dead": u"Утонувшие ифритки:",
    "underwater_giant_dead_1": u"Утонувшие великанши:",
    "underwater_giant_dead_2": u"Великанши, погибшие в битве с гигантским кальмаром:",
    "underwater_mermaid_dead": u"Русалки, погибшие в битве с гигантским кальмаром:",
    "underwater_usual_dead_1": u"Утонувшие из-за неожиданной судороги:",
    "underwater_usual_dead_2": u"Утонувшие из-за неумения плавать:",
    "underwater_usual_dead_3": u"Унесённые в открытый океан мощным течением:",
    "underwater_usual_dead_4": u"Застигнутые штормом в открытом океане:",
    "underwater_usual_dead_5": u"Погибшие в битве с гигантским кальмаром:",
    "whipped": u"Горожанки, запоротые до смерти:",
}

live_reason_explain = {  # Описание последствий жизни
    "berries": [u"А мне её ягоды так понравились, что я её отпустил!",'berries'],
    "blind_elf": [u"После ослепления у альвы открылось Внутренне зрение, и она стала Видящей.",'blind'], 
    "blind_fire": [u"После ослепления у ифритки открылось Внутренне зрение, и она стала кахином.",'blind'], 
    "blind_ice": [u"После ослепления у йотунши открылось Внутренне зрение, и она стала вёльвой.",'blind'], 
    "blind_mermaid": [u"После ослепления у морской девы открылось Внутренне зрение, и она стала ведуньей.",'blind'], 
    "blind_ogre": [u"После ослепления у огрши открылось Внутренне зрение, вот только она никому в этом не призналась.",'blind'], 
    "blind_princess": [u"После ослепления у аристократки открылось Внутренне зрение, и она стала оракулом.",'blind'],
    "blind_titan": [u"После ослепления у титаниды открылось Внутренне зрение, и она стала пифией.",'blind'], 
    "cripple_alchemist": [u"Она с ящериком связалась, я её за это искалечил, а этот поганец потом с помощью алхимика для неё протезы сделал!",'cripple_luck'],
    "cripple_demon": [u"Она с ящериком связалась, я её за это искалечил, а этот поганец потом с помощью культистов архитота для неё протезы сделал!",'cripple_luck'], 
    "dark_whore": [u"Она с ящериком связалась и вместе с ним к Тёмной Госпоже сбежала, ну и стала там аппаратом для производства отродий.",'dark_whore'],
    "elf_brothel":[u"А эта альва благополучно домой вернулась, а потом ей так секса захотелось, что она стала одной из самых известных куртизианок Королевства.",'prostitute'], 
    "elf_raped": [u"А эта альва благополучно в свой лес вернулась, а потом погрузилась в длительную депрессию.",'raped'], 
    "elf_virgin": [u"А эта альва благополучно в свой лес вернулась и вышла замуж за какого-то друида.",'marry'], 
    "elf_warrior": [u"А эта альва благополучно в свой лес вернулась и стала воительницей.",'warrior'],  
    "marrige_to_knight": [u"А её рыцарь спас, и она за него замуж вышла.",'marrige_to_knight'], 
    "mermaid_brothel": [u"А эта русалка благополучно домой вернулась, а потом ей так секса захотелось, что она стала случайных путников соблазнять.",'prostitute'], 
    "mermaid_raped": [u"А эта русалка благополучно домой вернулась, а потом погрузилась в длительную депрессию.",'raped'], 
    "mermaid_warrior": [u"А эта русалка благополучно домой вернулась и стала воительницей.",'warrior'], 
    "monastery": [u"А она с чего-то расстроилась и в монастырь ушла",'monastery'],
    "princess_brothel": [u"А эта аристократка благополучно домой вернулась, а потом ей так секса захотелось, что она устроилась в самый дорогой столичный бордель.",'prostitute'], 
    "princess_virgin": [u"А эта аристократка благополучно вернулась домой и вышла замуж за прекрасного принца.",'marry'], 
    "princess_warrior": [u"А эта аристократка благополучно домой вернулась и стала воительницей.",'warrior'], 
    "return_fire": [u"Ифритка благополучно вернулась домой. Что с ней станется, с великаншей-то?",'giant'], 
    "return_ice": [u"Йотунша благополучно вернулась домой. Что с ней станется, с великаншей-то?",'giant'], 
    "return_mermaid": [u"А эта русалка благополучно вернулась домой и вышла замуж за тритона.",'marry'], 
    "return_ogre": [u"Огрша благополучно вернулась домой. Что с ней станется, с великаншей-то?",'giant'],
    "return_siren": [u"Сирена благополучно вернулась домой. Что с ней станется, с великаншей-то?",'giant'], 
    "return_titan": [u"Титанида благополучно вернулась домой. Что с ней станется, с великаншей-то?",'giant'], 
    "sultan_fate": [u"А она попала в Султанат и стала любимой женой в гареме.",'sultan'], 
    "sultan_normal": [u"А она попала в Султанат и прожила тихую и непритязательную жизнь в гареме.",'sultan'],	
    "uncle_elf":  [u"А эта альва с ящериком связалась и вместе с ним к своему дяде сбежала, ну и стала там жить-поживать да детишек наживать.",'uncle'],
    "uncle_princess": [u"А эта аристократка с ящериком связалась и вместе с ним к своему дяде сбежала, ну и стала там жить-поживать да детишек наживать.",'uncle'],
    "victory": [u"Мне... стыдно об этом говорить...",'victory'], 
}

live_reason_desc = {  # Описание последствий жизни
    "berries": u"Крестьянки с корзинками, отпущенные драконом:",
    "brothel_girl": u"Проституки, начавшие свою карьеру с ночи с драконом:",
    "willing_girl": u"Спасена драконом от несчастных случаев (<= договор с драконом)",
    "blind_citizen": u"Слепые горожанки, ставшие пророчицами:",
    "blind_elf": u"Слепые альвы, ставшие Видящими своего народа:",
    "blind_fire": u"Слепые ифритки, ставшие кахинами:",
    "blind_ice": u"Слепые йотунши, ставшие вёльвами:",
    "blind_mermaid": u"Слепые морские девы, ставшие ведуньями:",
    "blind_ogre": u"Слепые огрши, так и не поведовавшие никому о пророческом даре:",
    "blind_peasant": u"Слепые селянки, ставшие гадалками:",
    "blind_princess": u"Слепые аристократки, ставшие оракулами:",
    "blind_titan": u"Слепые титаниды, ставшие пифиями:",
    "citizen_brothel": u"Развращённые горожанки:",
    "citizen_married": u"Горожанки, счастливо вышедшие замуж:",
    "citizen_warrior": u"Горожанки, ставшие воительницами:",
    "cripple_alchemist": u"Калеки, возвращённые к подобию нормальной жизни безумным алхимиком:",
    "cripple_demon": u"Калеки, излеченные последователями Архитота и присоединившиеся к кульу:",
    "dark_whore": u"Нашедшие своё место в войске Тёмной Госпожи:",
    "deAd_bdsm": u"Рыжие ведьмы, оставшиеся в пыточной замка де Ада:",
    "deAd_couple": u"Рыжие ведьмы, вышедшие замуж за маркиза де Ада:",
    "deAd_elf_madness": u"Коварные альвы, объединившиеся с Тёмными сёстрами:",
    "deAd_pass": u"Рыжие ведьмы, пропавшие во время тайного проникновения в замок де Ада:",
    "deAd_talk": u"Рыжие ведьмы, пропавшие во время штурма замка де Ада:",
    "deAd_sisters": u"Рыжие ведьмы, помирившиеся со своими сёстрами:",
    "elf_brothel": u"Развращённые альвы:",
    "elf_raped": u"Отчаявшиеся альвы, вернувшиеся домой:",
    "elf_virgin": u"Альвы, счастливо вернувшиеся домой:",
    "elf_warrior": u"Альвы, ставшие воительницами:",
    "marrige_to_knight": u"Пленницы, спасённые рыцарем и вышедшие за него замуж:",
    "mermaid_brothel": u"Развращённые русалки:",
    "mermaid_raped": u"Отчаявшиеся русалки, вернувшиеся домой:",
    "mermaid_warrior": u"Русалки, ставшие воительницами:",
    "monastery": u"Ушедшие в монастырь:",
    "peasant_brothel": u"Развращённые крестьянки:",
    "peasant_virgin": u"Крестьянки, счастливо вышедшие замуж:",
    "peasant_warrior": u"Крестьянки, ставшие воительницами:",
    "princess_brothel": u"Развращённые аристократки:",
    "princess_virgin": u"Аристократки, счастливо вышедшие замуж:",
    "princess_warrior": u"Аристократки, ставшие воительницами:",
    "rebel": u"Предводительницы восстания, предположительно укрыввшиеся на острове контрабандистов:",
    "return_fire": u"Ифритки, вернувшиеся домой:",
    "return_ice": u"Йотунши, вернувшиеся домой:",
    "return_mermaid": u"Русалки, счастливо вернувшиеся домой:",
    "return_ogre": u"Огрши, вернувшиеся домой:",
    "return_siren": u"Сирены, вернувшиеся домой:",
    "return_titan": u"Титаниды, вернувшиеся домой:",
    "sultan_fate": u"Ставшие любимыми женами в гареме:",
    "sultan_normal": u"Прожившие тихую и непритязательную жизнь в гареме:",
    "uncle_citizen": u"Горожанки, вместе с возлюбленным вернувшиеся к дяде:",
    "uncle_elf": u"Альвы, вместе с возлюбленным вернувшиеся к дяде:",
    "uncle_peasant": u"Крестьянки, вместе с возлюбленным вернувшиеся к дяде:",
    "uncle_princess": u"Аристократки, вместе с возлюбленным вернувшиеся к дяде:",
    "victory": u"Вместе с возлюбленным победившие дракона и устроившиеся жить в его логове:",
}

game_events = {
    "mobilization_increased": "lb_event_mobilization_increase",
    "poverty_increased": "lb_event_poverty_increase",
    "no_thief": "lb_event_no_thief",    # Не было активного вора и новый не нашелся
    "no_knight": "lb_event_no_knight",  # Не было активного рыцаря и новый не нашелся
    "sleep_start": "lb_event_sleep_start",
    "sleep_new_year": "lb_event_sleep_new_year",
    "sleep_end": "lb_event_sleep_end",
}

dark_army = {
    "grunts": {
        0: u"После поражения Госпожи в Битве Шести Воинств от её армии остались жалкие ошмётки. "
           u"Немногие выжившие гоблины прячутся по своим пещерам и "
           u"размножаются, словно кролики, в попытке пополнить ряды войск. ",
        10: u"Хорошая новость: на бесплодных равнинах собралось достаточно агрессивных тварей, "
           u"чтобы из них можно было собрать настоящее войско. "
           u"Плохая: это войско будет уступать по численности тому, что могут собрать Вольные Народы.",
        25: u"Пещер и дыр уже не хватает, чтобы дать укрытие всем уродливым воинам, живущим под рукой Госпожи. "
            u"Бесплодные равнины стали местом огромной стройки - тут и там возникают целые городки из шатров, "
            u"трудолюбиво окружаемые рвами, насыпями и частоколами. "
            u"На первый взгляд бойцов тут не меньше, чем может выставить на поле коалиция Вольных Народов.",
        50: u"Взглянув на бесплодные равнины в ночи, трудно понять, где кончается усыпанное звёздами небо и "
            u"начинается выгоревшая земля с мириадами костров, дающих свет и тепло воинам Госпожи. "
            u"Днём можно увидеть многие тысячи шатров, покрывающие долину словно заросли ядовитых грибов. "
            u"Тут и там снуют вестовые и дозорные. "
            u"Эта огромная Орда захлестнёт малочисленные войска Вольных Народов словно морской прибой."
    },
    "elites": {
        0: u"Но каково бы не было количество этих войск, их главной слабостью является отсутствие элитных бойцов. "
           u"Столкнувшись на поле боя с великанами, магами альвов и боевыми машинами цвергов, "
           u"Госпожа поняла, что противостоять им смогут лишь существа "
           u"многократно превосходящие по силе людей или гоблинов. Именно таких должны породить драконы. "
           u"Именно в них отчаянно нуждается войско Госпожи.",
        1: u"Тут и там можно заметить огромные силуэты элитных бойцов. "
           u"Их тут немного, однако в ключевой момент они встанут на острие атаки. ",
        5: u"На каждый отряд мелких тварей вроде гоблинов, тут приходится хотя бы один элитный боец, "
           u"порождённый драконом от самой сильной крови Вольных Народов. "
           u"Каждый их этих могучих гигантов сам стоит в бою целой армии.",
        10: u"В этом войске столько элитных бойцов, "
           u"что обычная мелочь вроде гоблинов служит лишь для разведки и поддержки их действий. "
           u"Ударную мощь обеспечивают уродливые гиганты, порождённые драконами от самой могучей крови Вольных Народов."
    },
    "diversity": {
        0: u"Армия тьмы не отличается разнообразием, "
           u"подавляющее большинство бойцов относится к одному единственному виду. "
           u"Воины Вольных Народов уже отлично умеют сражаться с такими тварями и "
           u"обладают отработанной тактикой против них.",
        2: u"Разнообразие войск не слишком велико, "
           u"хотя порождения драконов будут выгодно дополнять обычных гоблинов на поле боя. "
           u"Тем не менее, Вольным Народам не составит труда выработать тактику противодействия и "
           u"изучить сильные и слабые места всех бойцов Госпожи.",
        4: u"Порождения драконов, собравшиеся под знамёна Госпожи, очень разнообразны. "
           u"Здесь есть дылды и коротышки, стремительные лазутчики и массивные штурмовики, всех цветов, размеров и форм. "
           u"Кого-то украшает чешуая, кого-то рога. "
           u"Выгодно дополняя друг друга на поле боя, "
           u"вся эта пёстрая компания не позволит Вольным Народам использовать простую и привычную тактику боя.",
        7: u"Тут столько разнообразных тварей, что, наверное, даже сама Госпожа не сможет различить их всех. "
           u"Бесконтрольно смешиваясь между собой, "
           u"отродья драконов порождают новые мутантные гибриды с невероятными свойствами. "
           u"Когда начнётся война, Вольные Народы не будут знать, как бороться с ними."
    },
    "equipment": {
        1: u"Денег на снаряжение армии катастрофически не хватает. Воины Госпожи ходят в одних набедренных повязках, "
           u"вооружаются кривыми дубинами и заострёнными палками вместо копий. "
           u"Только некоторые могут позволить себе грубую броню из плохо обработанных шкур.",
        2: u"Армия снаряжена по минимуму. Рядовые воины могут надеяться получить железное копьё, "
           u"плетёный щит и простой стёганный доспех. Элита вооружается чуть лучше, но всё же картина далека от желаемой.",
        3: u"Сокровища драконов позволили неплохо снарядить бойцов Госпожи. "
           u"Даже у рядовых воинов есть полный комплект вооружения и брони, "
           u"а элита закована в воронёную сталь с ног до головы. "
           u"Ряды чёрных пик и щитов на поле боя будут смотреться очень внушительно.",
        4: u"За долгие годы драконы скопили для Госпожи такую кучу сокровищ, "
           u"что её с лихвой хватает для вооружения всей армии по самому высшему разряду. "
           u"Тяжёлая пехота и кавалерия вооружена до зубов, а элитные бойцы щеголяют волшебным оружием и доспехами. "
    },
    "force": {
        0: u"Выступать с такими силами против Вольных Народов будет просто самоубийством. Разве что дракон сам выиграет все битвы.",
        500: u"Хотя армия тьмы и окрепла за последние годы, к битве с Вольными Народами она пока не готова. Дракону придётся брать основной удар на себя в каждом бою, чтобы иметь хоть какие-то шансы.",
        1000: u"В общем и целом Армия Тьмы достаточно боеспособна, чтобы иметь шансы в битвах с войском Вольных Народов. "
              u"Однако полной уверенности в победе быть не может. Дракон должен будет поддержать свои войска личным примером.",
        1800: u"За долгие годы подготовки Армия Тьмы не просто воспаряла, но и стала могущественнее, чем когда-либо. "
              u"Войско Вольных Народов будет смято и растоптано этой неодолимой силой. Даже не учитывая помощи, которую могут лично оказать Дракон и сама Владычица."
    }
}

last_enemies = {
    "dagon": {
        "image": "img/scene/fight/dagon.jpg",
        "win": u"Атаковать древнего бога, поднявшегося из морских глубин - настоящее безумие. Тем не менее, воины армии тьмы занимались именно этим. Дагон, не выказывая ни малейших признаков усталости, смывал их в пучину десяток за десятком, сотню за сотней. А потом, в какой-то момент, ему это надоело, и божество, бормоча себе под нос 'Воистину фхтагн', ушло домой - спать дальше. ",
        "loss": u"Атаковать древнего бога, поднявшегося из морских глубин - настоящее безумие. Дагон за один присест смыл в море всю армию тьмы ",
        "name": u"Дагон",
        "name_r": u"Дагона",
        "name_t": u"Дагоном",
        "afrodita": u"Афродита нежно касается своей рукой кожи Древнего бога. В первый момент Дагон недовольно булькает, но потом начинает довольно урчать и в конце концов ныряет в пучину вод, утащив с собой Афродиту. ",
        "danu": u"Дану бесстрашно подходит к Древнему богу и начинает напевать негромкую колыбельную. Дагон сонно урчит и через некоторое время ныряет в пучину вод, не забыв утащить с собой Дану. ",
    },
    "athena": {
        "image": "img/scene/athena_ready.jpg",
        "win": u"Копьё Афины разило без промаха, а круглый щит-эгида защищал, казалось, от любых атак. Богиня войны могла в одиночку уничтожить всю Армию тьмы - и, что самое плохое, собиралась это сделать. А потом какой-то тролль метким ударом дубины сшиб с её плеча сову. Богиня запаниковала, выхватила свою питомицу из лап минотавров и убралась обратно на Олимп. Кажется, богам и в самом деле нет дела до участи смертных...",
        "loss": u"Копьё Афины разит без промаха, а круглый щит-эгида защищает от любых атак. Смертным не стоит бросать вызов богам - Афина Паллада легко и непринуждённо в одиночку уничтожила всю армию тьмы. ",
        "name": u"Афина",
        "name_r": u"Афину",
        "name_t": u"Афиной",
        "danu": u"С рук Дану струится бесконечный поток магической энергии. Афина, прикрываясь щитом, с трудом подходит к богине альвов и наносит неотразимый и смертоносный удар копьём. Впрочем, битва дорого обошлась Палладе. Шатаясь, она исчезает во внезапно сгустившимся мареве. Похоже, олимпийцы не готовы оборонять Столицу 'до последнего вздоха', раз уж при первом признаке опасности стремятся убраться на Олимп! ",
    },
    "angel": {
        "image": "img/scene/fight/angel.jpg",
        "win": u"Исчадия Тьмы выпускают в ангела сотни стрел, но они сгорают на подлёте. Небесный страж рубит отряды гоблинов своим мечом, словно скашивая пожухлую траву серпом. Наконец, его удаётся сбить метким выстрелом тяжёлой катапульты, но потери очень велики.",
        "loss": u"Исчадия Тьмы выпускают в ангела сотни стрел, но они сгорают на подлёте. Небесный страж рубит отряды тёмных тварей своим мечом, словно скашивая пожухлую траву серпом. С каждой минутой сопротивление армии тьмы слабеет и слабеет, пока её жалкие остатки не бегут прочь в страхе. Но ангел не дал им уйти. Он спокойно и размеренно закончил свою работу",
        "name": u"Ангел",
        "name_r": u"Ангела",
        "name_t": u"Ангелом",
        "afrodita": u"Афродита бесстрашно встаёт на пути ангела, преграждая дорогу к дракону и армии тьмы. Посланник Небес несколько раз, всё настойчивей и настойчивей требует удалиться, но Афродита отвечает лишь звонким смехом. В конце концов ангел пронзил её сердце огненным мечом. Выполнив свой долг, посланник Небес исчез в столпе света, ибо на этот раз долг вошёл в противоречие с совестью.",
        "danu": u"Дану кидается на ангела. Ослепительная вспышка... и всё. Ни посланника Небес, ни богини альвов больше нет.",
    },
    "golem": {
        "image": "img/scene/fight/golem.jpg",
        "win": u"Железного голема удаётся буквально похоронить под грудой мяса и железа, в которые превращаются идущие волна за волной в самоубийственную атаку Исчадия Тьмы. Тем не менее это победа!",
        "loss": u"Камень и железо сильнее бренной плоти. Голем ещё раз подтвердил эту истину, в одиночку уничтожив большую часть армии тьмы. Когда отродья дракона бежали прочь, на поверхности голема осталось лишь несколько глубоких царапин.",
        "name": u"Голем",
        "name_r": u"Голема",
        "name_t": u"Големом",
        "afrodita": u"Афродита несколько секунд смотрела на непобедимого голема цвергов, а потом неожиданно сама превратилась в каменную статую. Два голема некоторое время стояли друг напротив друга, а потом взялись за руки и пошли в сторону гор. Любовь способна одолеть даже камень!",
        "danu": u"Голем равнодушно наступает на Дану - и в следующее же мгновение побеги растений прорастают сквозь монолит, дробя на части казавшуюся несокрушимой фигуру. \n\nСудя по произошедшему, война альвов со цвергами не за горами...",
    },
    "treant": {
        "image": "img/scene/fight/treant.jpg",
        "win": u"Срубить гигантское дерево, активно отмахивающееся корнями и ветками, непросто. Но, понеся огромные потери, Армия тьмы справилась и с этой нетривиальной задачей.",
        "loss": u"Корни чащобного стража раз за разом переводили тёмных тварей на гумус. И, что ещё хуже, из плоти погибших проклёвывались новые ростки. Скоро на площади поднялась небольшая рощица, а армия тьмы канула в прошлое.",
        "name": u"Чащобный страж",
        "name_r": u"Чащобного стража",
        "name_t": u"Чащобным стражем",
        "afrodita": u"Чащобный страж равнодушно смахнул Афродиту со своего пути. Но не тут-то было - его ветки прочно застряли в теле дико кричащей Афродиты. Трент попытался избавиться от тела богини, но с каждым мгновением его движения становились всё медленне и медленнее. Вскоре Афродита полностью растворилась в древесине, а на площади перед дворцом росло высокое раскидистое дерево.",
    },
}

#Achievements
def achieve_target(target, tag=None):
    for achievement in achievements_list:
        if tag == "wealth" or tag == "treasure" or tag == "reputation":
            if achievement.goal == tag:
                    achievement.progress(target)
        elif achievement.goal == tag and target in achievement.targets:
            achievement.progress(target)
def achieve_restart(reason):
    for achievement in achievements_list:
        if achievement.restartif == reason:
            achievement.restart()
def achieve_fail(reason):
    for achievement in achievements_list:
        if achievement.failif == reason:
            achievement.fail()
def achieve_win(dragon):
    achieve_target("win", "win")
    if dragon.size > 1:
        achieve_fail("too_big")
    if dragon.magic > 0:
        achieve_fail("dragon_magic")
    for n in xrange(dragon.size):
        achieve_target("size", "win")
    for head in dragon.heads:
        if head != "green":
            achieve_target("colored_head", "win")
        achieve_target("head", "win")
    if dragon.wings == 1 and dragon.paws == 2 and len(dragon.heads) == 1:
        achieve_target("archetype", "win")
    else:
        achieve_target(dragon.kind, "win")
    achieve_target(dragon.color_eng, "win")
def store_achievements(storage_dict):
    temporary_storage = {}
    for achievement in achievements_list:
        if achievement.unlocked and achievement.name not in storage_dict.keys():
            storage_dict[achievement.name] = achievement.description
            temporary_storage[achievement.name] = achievement.description
    return temporary_storage
class Achievement(object):
    def __init__(self, name="", description="", goal=None, targets=None, restartif=None, failif=None, *args, **kwagrs):
        self.name = name
        self.description = description
        self.unlocked = False
        self.failed = False
        self.restartif = restartif
        self.failif = failif
        self.goal = goal
        self.targets = targets
        self.targets_completed = []
    def progress(self, target):
        if self.failed:
            return
        if self.targets:
            if self.goal == "wealth" or self.goal == "treasure" or self.goal == "reputation":
                for i in self.targets:
                    if target >= i:
                        self.targets.remove(i)
                        self.targets_completed.append(i)
                
            else:
#                game.history = historical( name=target,end_year=None,desc=None,image=None)
#                self.game.history_mod.append(self.game.history)
                self.targets_completed.append(target)
                self.targets.remove(target)
                
                    
        if not self.targets and not self.unlocked:
            self.unlock()
    def unlock(self):
        if not self.failed:
            self.unlocked = True
    def fail(self):
        self.failed = True
    def restart(self):
        if not self.unlocked and self.targets_completed:
            self.targets.extend(self.targets_completed)
            self.targets_completed = []

achievements_list = [Achievement(name = u"Великий змей",
                                 description = u"Достиг победы в сюжетном режиме",
                                 goal = "win",
                                 targets = ["win"]),
                     Achievement(name = u"Осквернитель",
                                 description=u"Сделал логово в Зачарованном лесу",
                                 goal = "lair",
                                 targets = ["forest_heart"]),
                     Achievement(name = u"Смауг Великолепный",
                                 description = u"Сделал логово в подгорных чертогах",
                                 goal = "lair",
                                 targets = ["underground_palaces"]),
                     Achievement(name = u"Великолепное ложе",
                                 description = u"Достиг суммарной стоимости сокровищ 100.000 фартингов",
                                 goal = "wealth",
                                 targets = [100000]),
                     Achievement(name = u"Венец коллекции",
                                 description = u"Иметь в сокровищнице предмет стоимостью больше 3000 фартингов",
                                 goal = "treasure",
                                 targets = [9000]),
                     Achievement(name = u"Легендарный тиран",
                                 description = u"Достичь уровня дурной славы больше 19",
                                 goal = "reputation",
                                 targets = [19]),
                     Achievement(name = u"Осеменитель",
                                 description = u"Спарился со всеми видами не-великанш, играя за одного дракона",
                                 goal = "impregnate",
                                 targets = ["peasant", "citizen", "princess", "elf", "mermaid"], #вернуть когда появятся  "thief", "knight",
                                 restartif = "new_dragon"),
                     Achievement(name = u"Отец титанов",
                                 description = u"Спарился со всеми видами великанш, играя за одного дракона",
                                 goal = "impregnate",
                                 targets = ["ice", "fire", "titan", "ogre", "siren"],
                                 restartif = "new_dragon"),
                     Achievement(name = u"Неуязвимый",
                                 description = u"Достиг победы в сюжетном режиме, не потеряв ни одной головы",
                                 goal = "win",
                                 targets = ["win"],
                                 failif = "lost_head"),
                     Achievement(name = u"Абсолютный хищник",
                                 description = u"Победить ангела, титана и железного голема одним и тем же драконом",
                                 goal = "kill",
                                 targets = ["golem", "angel", "titan"],
                                 restartif = "new_dragon"),
                     Achievement(name = u"Дитя предназначения",
                                 description = u"Выиграть игру захватом земель вольных народов и остаться верным Тёмной Госпоже",
                                 goal = "win",
                                 targets = ["conquer"]),
                     Achievement(name = u"Иуда",
                                 description = u"Выиграть игру, предав Тёмную Госпожу и победив её в битве",
                                 goal = "win",
                                 targets = ["betray"]),
                     Achievement(name = u"Архетип",
                                 description = u"Достиг победы в сюжетном режиме с подтипом: дракон",
                                 goal = "win",
                                 targets = ["archetype"]),
                     Achievement(name = u"Йормунгард",
                                 description = u"Достиг победы в сюжетном режиме одноглавым синим драконом, не имеющем крыльев и конечностей",
                                 goal = "win",
                                 targets = [u"ползучий гад","blue"]),
                     Achievement(name = u"Змей горыныч",
                                 description = u"Достиг победы в сюжетном режиме с подтипом: многоглавый дракон",
                                 goal = "win",
                                 targets = [u"многоглавый дракон"]),
                     Achievement(name = u"Наследие Тиамат",
                                 description = u"Достиг победы драконом с 3+ разными цветами",
                                 goal = "win",
                                 targets = ["colored_head", "colored_head", "colored_head"]),
                     Achievement(name = u"Лернейская гидра",
                                 description = u"Достиг победы с 4+ головами",
                                 goal = "win",
                                 targets = ["head", "head", "head", "head"]),
                     Achievement(name = u"Левиафан",
                                 description = u"Достиг победы драконом максимального размера",
                                 goal = "win",
                                 targets = ["size", "size", "size", "size", "size", "size"]),
                     Achievement(name = "T-Rex",
                                 description = u"Достиг победы зеленым линдвурмом без магии, с одной головой и размером больше 4",
                                 goal = "win",
                                 targets = ["size", "size", "size", "size", u"линдвурм", "green"],
                                 failif = "dragon_magic"),
                     Achievement(name = u"Годзила",
                                 description = u"Достиг победы красным линдвурмом с размером больше 4",
                                 goal = "win",
                                 targets = ["size", "size", "size", "size", u"линдвурм", "red"]),
                     Achievement(name = u"Фейский дракончик",
                                 description = u"Достиг победы драконом самого маленького размера",
                                 goal = "win",
                                 targets = ["size"],
                                 failif = "too_big"),
                     Achievement(name = u"Недрёмное око",
                                 description = u"Достиг победы, не потеряв ни одного сокровища из-за воров или рыцарей",
                                 goal = "win",
                                 targets = ["win"],
                                 failif = "lost_treasure"),
                     Achievement(name = u"Пасхальный кролик",
                                 description = u"Собрать все пасхалки",
                                 goal = "easter_eggs",
                                 targets = ["domiki_done", "redhood_done"]),
                     Achievement(name = u"Караванная тропа",
                                 description = u"Наладить торговлю с Султанатом",
                                 goal = "sultan_trade",
                                 targets = ["hakim"]),
                     Achievement(name = u"Свет далёкой звезды",
                                 description = u"Отвергнуть милосердие огненной ведьмы и спастись бегством",
                                 goal = "kill",
                                 targets = ["fire_witch"]),
                     Achievement(name = u"Легион. Покорит. Вселенную",
                                 description = u"Узреть Князя Ада Архитота",
                                 goal = "architot",
                                 targets = ["seen"]),
                     Achievement(name = u"Devil may cry",
                                 description = u"Убить Архитота",
                                 goal = "win",
                                 targets = ["architot"]),
                     Achievement(name = u"Губитель",
                                 description = u"Убить более 99% всех встреченных девушек",
                                 goal = "win",
                                 targets = ["killer"]),
                     Achievement(name = u"Аспект милосердия",
                                 description = u"Убить менее 1% всех встреченных девушек",
                                 goal = "win",
                                 targets = ["saver"]),
                     Achievement(name = u"МС-н{i}О{/i}гибатор",
                                 description = u"Выиграть игру захватом земель вольных народов и сломить Тёмную Госпожу, полностью подчинив её своей воле",
                                 goal = "win",
                                 targets = ["MC"]),
                     Achievement(name = u"Пришёл. Увидел. Победил",
                                 description = u"Во время Последней битвы захватить королевский дворец без боя",
                                 goal = "battle",
                                 targets = ["vini_vidi_vici"]),
                     Achievement(name = u"Драконий блицкриг",
                                 description = u"Во время Последней битвы взять штурмом Столицу сразу после победы в генеральном сражении",
                                 goal = "battle",
                                 targets = ["bliz"]),
                     Achievement(name = u"Свет торжествует",
                                 description = u"Вольные одержали полную и окончательную победу",
                                 goal = "battle",
                                 targets = ["mistress"]),
                     Achievement(name = u"Целую, Фиалка",
                                 description = u"Месть принцессы Фиалки свершилась",
                                 goal = "battle",
                                 targets = ["jasmine"]),
                    ]
