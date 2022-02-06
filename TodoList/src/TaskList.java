package TodoList.src;

import java.util.ArrayList;

public class TaskList extends ArrayList<Task>
{
    public TaskList()
    {
        super();
    }

    public String toJSONString()
    {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < this.size(); i++)
        {
            sb.append(this.get(i).toJSONString());
            if (i != this.size() - 1)
            {
                sb.append(",\n");
            }
        }
        sb.append("\n]");
        return sb.toString();
    }

    public String toString()
    {
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < this.size(); i++)
        {
            sb.append((i + 1));
            sb.append(". ");
            sb.append(this.get(i));
            sb.append("\n");
        }
        return sb.toString();
    }
}
