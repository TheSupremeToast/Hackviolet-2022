package TodoList.src;

import java.util.Date;
import java.util.ArrayList;


public class Task
{
    ArrayList<SubTask> subtasks;
    String name;
    Date date;

    public Task(String name, Date date)
    {
        this.subtasks = new ArrayList<>();
        this.name = name;
        this.date = date;
    }

    public void addSubtask(SubTask subTask)
    {
        subtasks.add(subTask);
    }

    public void deleteSubtask(int position)
    {
        subtasks.remove(position - 1);
    }

    public String toJSONString()
    {
        StringBuilder sb = new StringBuilder();
        sb.append("{\n\t");
        sb.append("\"taskName\" : ");
        sb.append("\"" + name + "\"");
        sb.append(",\n\t");
        sb.append("\"taskDate\" : ");
        sb.append("\"" + date + "\"");
        for (int i = 0; i < subtasks.size(); i++)
        {
            sb.append(",\n\t");
            sb.append("\"subtask" + (i + 1));
            sb.append("\" : ");
            sb.append("\"" + subtasks.get(i).toString() + "\"");
        }
        sb.append("\n}");
        return sb.toString();
    }

    public String toString()
    {
        StringBuilder sb = new StringBuilder();
        sb.append(name);
        sb.append(" ");
        sb.append(date.toString());
        sb.append("\n");
        for (int i = 0; i < subtasks.size(); i++)
        {
            sb.append("\t");
            sb.append(i + 1);
            sb.append(". ");
            sb.append(subtasks.get(i));
            sb.append("\n");
        }
        return sb.toString();
    }
}
