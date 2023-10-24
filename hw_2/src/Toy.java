public class Toy {
    private int id;
    private static int generalId;
    private String name;
    private int count;
    private int weight;

    public Toy(String name, int count, int weight) {
        generalId++;
        this.id = generalId;
        this.name = name;
        this.count = count;
        this.weight = weight;
    }

    public void cutCount() {
        count--;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "ID: " + id + "; Name: " + name;
    }
}
