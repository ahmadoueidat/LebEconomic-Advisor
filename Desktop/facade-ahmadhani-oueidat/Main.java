public class Main {
    public static void main(String[] args) {
        CheckoutFacade checkout = new CheckoutFacade();

        boolean success = checkout.placeOrder(
                "Laptop", 1, "ACC-123", 999.99,
                "Beirut, Lebanon", "student@example.com");

        System.out.println(success ? "Order succeeded" : "Order failed");
    }
}
