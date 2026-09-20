public class PaymentService {
    public boolean charge(String account, double amount) {
        System.out.println("Charging " + account + ": " + amount);
        return true; // change to false to test a declined payment
    }
}
