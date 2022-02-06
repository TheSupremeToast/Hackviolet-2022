package TodoList.src;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

public class Main
{
    public static Scanner scan;
    public static String scanResult;
    public static TaskList taskList;

    public static void main(String [] args) throws IOException
    {
        taskList = new TaskList();
        scan = new Scanner(System.in);
        do
        {

            System.out.println("Please enter a command (see 'help' for list of commands): ");
            scanResult = scan.next();
            if (scanResult.equals("help"))
            {
                help();
            }
            else if (scanResult.equals("create"))
            {
                create();
            }
            else if (scanResult.equals("delete"))
            {
                delete();
            }
            else if (scanResult.equals("list_tasks"))
            {
                list_tasks();
            }
        } while (!scanResult.equals("exit"));
        toJSON();
    }

    public static void help()
    {
        System.out.println("help - lists all of the commands");
        System.out.println("create - create a new task or subtask");
        System.out.println("delete - delete an existing task or subtask");
        System.out.println("list tasks - lists all of the tasks and their subtasks");
    }

    public static void create()
    {
        scanResult = scan.next();
        if (scanResult.equals("subtask"))
        {
            create_subtask();
        }
        else if (scanResult.equals("task"))
        {
            create_task();
        }
    }

    public static void delete()
    {
        scanResult = scan.next();
        if (scanResult.equals("subtask"))
        {
            delete_subtask();
        }
        else if (scanResult.equals("task"))
        {
            delete_task();
        }
    }

    public static void list_tasks()
    {
        System.out.println(taskList);
    }

    public static void create_subtask()
    {
        int taskToGet = scan.nextInt();
        taskList.get(taskToGet - 1).addSubtask(new SubTask(scan.next()));
    }

    public static void delete_subtask()
    {
        int taskToGet = scan.nextInt();
        taskList.get(taskToGet - 1).deleteSubtask(scan.nextInt());
    }

    public static void create_task()
    {
        taskList.add(new Task(scan.next(), new Date(scan.nextInt(), scan.nextInt() - 1, scan.nextInt())));
    }

    public static void delete_task()
    {
        int taskToGet = scan.nextInt();
        taskList.remove(taskToGet - 1);
    }

    public static void toJSON() throws IOException
    {
        FileWriter fw = new FileWriter("user_data.json");
        fw.append(taskList.toJSONString());
        fw.close();
    }
}
