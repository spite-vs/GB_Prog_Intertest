import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class ToyMachine {
    private List<Toy> toylist = new ArrayList<>();

    public void addToy(Toy toy) {
        toylist.add(toy);
    }

    public Toy randomToy() {
        Random rand = new Random();

        for (Toy toy : toylist) {
            int i = rand.nextInt(100);
            if (toy.getCount() > 0 & i <= toy.getWeight()) {
                toy.cutCount();
                return toy;
            }
        }
        return null;

    }

    public void writerToy(Toy toy) {
        try {
            FileWriter fw = new FileWriter("WinList.txt", true);
            fw.write(toy.toString() + "\n");
            fw.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void changeWeight(int id, int newWeight) {
        for (Toy toy : toylist) {
            if (toy.getId() == id) {
                toy.setWeight(newWeight);
                return;
            }
        }
        System.out.println("Нет такой игрушки");
    }

    public List<Toy> getToylist() {
        return toylist;
    }
}
