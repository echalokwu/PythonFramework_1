class Locators:

    # Login Page Locators
    mobile_link_xpath = "//a[contains(text(),'Mobile')]"
    tv_link_xpath = "//a[contains(text(),'TV')]"
    sony_add_to_compare_link_xpath = "//li[1]//div[1]//div[3]//ul[1]//li[2]//a[1]"
    iphone_add_to_compare_link_xpath = "//li[2]//div[1]//div[3]//ul[1]//li[2]//a[1]"
    compare_link_xpath = "//button[@class='button']//span//span[contains(text(),'Compare')]"
    close_popUp_windows_link_xpath = "//span[contains(text(),'Close Window')]"

    main_window_sony = "//h2[@class='product-name']//a[contains(text(),'Sony Xperia')]"
    main_window_iphone = "//h2[@class='product-name']//a[contains(text(),'IPhone')]"

    new_window_sony = "//a[contains(text(),'Sony Xperia')]"
    new_window_iphone = "//a[contains(text(),'IPhone')]"
    confMessage = "//SPAN[text()='Thank you for registering with Main Website Store.']"
    add_product_to_wishList_xpath = "//li[1]//div[1]//div[3]//ul[1]//li[1]//a[1]"
    share_wishList_xpath = "//span[contains(text(),'Share Wishlist')]"
    share_List_email_id = "email_address"
    share_List_message_id = "message"

    myAccount_link_xpath = "//div[@class='footer']//a[contains(text(),'My Account')]"
    createAccount_link_xpath = "//span[contains(text(),'Create an Account')]"
    FirstName_text_id = "firstname"
    LastName_text_id = "lastname"
    Email_text_id = "email_address"
    Password_text_id = "password"
    PasswordConf_text_id = "confirmation"
    Register_button_xpath = "//span[contains(text(),'Register')]"
    actualWishlist = "//span[contains(text(),'Your Wishlist has been shared.')]"

    my_wish_link_xpath = "//div[@class='block-content']//a[contains(text(),'My Wishlist')]"
    login_button_xpath = "//span[contains(text(),'Login')]"
    add_to_cart_link_xpath = "//span[contains(text(),'Add to Cart')]"

    textRegistered_email_id = "email"
    textRegistered_password_id = "pass"


