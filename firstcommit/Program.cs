using System;
using System.IO;
using System.Diagnostics;
using System.Linq;
using System.Collections.Generic;

namespace firstcommit
{
    class MainClass
    {
        static string logFileName = "app.log";
        public static void Main(string[] args)
        {
            var curDir = "/G/DefilerWings";
            Directory.SetCurrentDirectory(curDir);

            Console.WriteLine($"Перешли в директорию {curDir}");
            File.WriteAllText(logFileName, "");

            for (var a = 32; a < 128; a++)
            {
                var astr = (char) a;
                var estr = new char[] { '*', '?', '"', '\'', '\\', '/' };
                if (estr.Contains(astr))
                    continue;

                var extensions = new string[] { $"*{astr}.py*", $"*{astr}.jpg", $"*{astr}.png", $"*{astr}.bin", $"*{astr}", $"{astr}*", "*" };
                foreach (var ext in extensions)
                {
                    // Пробуем * только в самом конце, чтобы не перечислять постоянно большое количество файлов
                    if (a < 127 && ext == "*")
                        continue;

                    ProcessStartInfo psi;
                    Process      pi;
                    var size = 0L;
                    while (true)
                    {
                        var cmd = $"add -nv \"{ext}\"";
    
                        psi  = new ProcessStartInfo("git", cmd);
                        psi.UseShellExecute        = false;
                        psi.RedirectStandardOutput = true;
                        psi.RedirectStandardError  = true;
    
                        StreamReader so = null;
                        pi = null;
                        try
                        {
                            // Console.WriteLine($"Start process \"git {cmd}\"");
                            pi = Process.Start(psi);
                            so = pi.StandardOutput;
                        }
                        catch
                        {
                            if (pi != null)
                                pi.WaitForExit();

                            break;
                        }
        
        
                        List<string> fList = new List<string>();
                        size = 0;
                        do
                        {
                            var line = so.ReadLine();
                            if (line == null)
                                break;
                            
                            line = line.Replace("add '", "");
                            line = line.Substring(0, line.Length - 1);

                            var fi = new FileInfo(line);
                            if (!fi.Exists)
                                throw new Exception("File not exists!!! It is impossible");

                            if (size > 0)
                            if (size + fi.Length > 8 * 1024 * 1024)
                                break;

                            size += fi.Length;
                            fList.Add(fi.FullName);

                            if (size > 8 * 1024 * 1024)
                                break;
                        }
                        while (true);

                        so.Close();
                        pi.WaitForExit();
                        pi.Close();
                        // Console.WriteLine($"add process ended with size {size}");

                        if (size <= 0)
                            break;

                        foreach (var name in fList)
                        {
                            cmd = $"add -v \"{name}\"";
                            using (var pia = Process.Start("git", cmd))
                            {
                                pia.WaitForExit();
                            }
                        }

                        // Console.WriteLine($"Commit start");

                        psi = new ProcessStartInfo("git", "commit -m \"-\"");
                        psi.UseShellExecute = false;
                        psi.RedirectStandardOutput = true;
                        psi.RedirectStandardError  = true;
                        pi  = Process.Start(psi);

                        pi.WaitForExit();
                        pi.Close();

                        Console.WriteLine();
                        Console.WriteLine();
                        Console.WriteLine($"To push {size/1024/1024}Mb");
                        Console.WriteLine();
                        Console.WriteLine();

                        psi  = new ProcessStartInfo("git", "push");
                        psi.UseShellExecute = false;
                        pi   = Process.Start(psi);

                        pi.WaitForExit();
                        pi.Close();

                        Console.WriteLine();
                        Console.WriteLine();
                    }
                }
            }
        }
    }
}
