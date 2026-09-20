public class CheckoutFacade {

    public boolean placeOrder(String item, int qty, String account,
                              double amount, String address, String email) {

        InventoryService inventory = new InventoryService();
        PaymentService payment = new PaymentService();
        ShippingService shipping = new ShippingService();
        NotificationService notification = new NotificationService();

        try {
            if (inventory.isAvailable(item, qty)) {
                if (payment.charge(account, amount)) {
                    shipping.schedule(item, address);
                    notification.sendConfirmation(email);
                    return true;
                } else {
                    System.out.println("Payment failed");
                    return false;
                }
            } else {
                System.out.println("Item not available");
                return false;
            }
        } catch (Exception e) {
            System.out.println("Order failed: " + e.getMessage());
            return false;
        }
    }
}
