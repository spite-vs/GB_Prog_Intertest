public class App {
    public static void main(String[] args) throws Exception {
        Toy t1 = new Toy("Конструктор", 15, 20);
        Toy t2 = new Toy("Робот", 5, 20);
        Toy t3 = new Toy("Кукла", 10, 15);
        Toy t4 = new Toy("Мяч", 8, 40);
        Toy t5 = new Toy("Слон", 2, 60);

        ToyMachine tm = new ToyMachine();
        tm.addToy(t1);
        tm.addToy(t2);
        tm.addToy(t3);
        tm.addToy(t4);
        tm.addToy(t5);

        tm.changeWeight(1, 10);
        tm.changeWeight(4, 10);

        for (int i = 0; i < 10; i++) {
            Toy prize = tm.randomToy();
            if (prize != null) {
                System.out.println("Вы выиграли: " + prize.getName());
                tm.writerToy(prize);
            } else {
                System.out.println("Повезёт в следующий раз");
            }
        }
        for (Toy toy : tm.getToylist()) {
            System.out.println(toy + "; Count: " + toy.getCount() + "; Chance: " + toy.getWeight());
        }
    }
}
