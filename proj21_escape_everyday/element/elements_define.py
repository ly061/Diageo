from selenium.webdriver.common.by import By

class ElementsDefine(object):
    """
    MY20 RYI Element Define
    """

    def __init__(self):
        """
        init function
        """
        #landingPage
        self.landing_country_select = (By.CSS_SELECTOR, "select.common_form-select") #country select
        self.landing_country_options = (By.CSS_SELECTOR, "select.common_form-select option")  # country select option
        self.landing_Go_button = (By.CSS_SELECTOR,"div.common-cta_btn") # Go button
        #homepage
        self.homepage_cookiemodel = (By.CSS_SELECTOR, "div.cookieModel p.cookieModel__title")
        self.homepage_cookiemodel_close = (By.CSS_SELECTOR, "div.cookieModel button.cookieModel__close")
        self.homepage_social_link = (By.CSS_SELECTOR, "div.footer__share-container a[target='_blank']")
        self.homepage_footer_link = (By.CSS_SELECTOR, "footer div.footer div.footer_links-container a")
        self.homepage_ryi_button = (By.CSS_SELECTOR, "div.home a.common-cta_btn.home__btn.active")
        self.homepage_footer_country_list = (By.CSS_SELECTOR, "footer div.footer div.common_form-ipt-container select.common_form-select option")

        #dealer page
        self.dealerpage_dealer_locate = (By.ID, "searchTextField")
        self.dealerpage_googlemap_suggestfirst = (By.CSS_SELECTOR, "div.pac-container div.pac-item")
        self.dealerpage_next_button = (By.CSS_SELECTOR, "#locationForm .googleMap__container button.common-cta_btn")

        #ryi-booking
        self.ryibooking_submit_button = (By.CSS_SELECTOR, "div.formModel div.common_sections button.common-cta_btn")
        self.ryibooking_form_errors = (By.CSS_SELECTOR, "div.formModel div.common_sections.form_error")

        #ryi-booking-popup
        self.ryibooking_privacy_page_link = (By.CSS_SELECTOR, "div.formModel div.common_sections p.paragraph__body-mid a.org-colored")
        self.ryibooking_privacy_first_popup = (By.CSS_SELECTOR, "div.formModel div.common_sections div.popup.firstPop")
        self.ryibooking_privacy_second_popup = (By.CSS_SELECTOR, "div.formModel div.common_sections div.popup.secondPop")
        self.ryibooking_privacy_first_popup_close = (By.CSS_SELECTOR, "div.formModel div.common_sections div.popup.firstPop div.popup__close")
        self.ryibooking_privacy_second_popup_close = (By.CSS_SELECTOR, "div.formModel div.common_sections div.popup.secondPop div.popup__close")

        # ryi-form-field
        self.ryibooking_form_title = (By.ID, "title")
        self.ryibooking_form_firstname = (By.ID, "firstName")
        self.ryibooking_form_lastname = (By.ID, "lastName")
        self.ryibooking_form_email = (By.ID, "email")
        self.ryibooking_form_mobile = (By.ID, "mobile")
        self.ryibooking_form_birthday = (By.ID, "birthDay")
        # licence has default value, ignore.
        self.ryibooking_form_motocycle = (By.ID, "myBikeName")
        self.ryibooking_form_viaemail = (By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='useEmail']")
        self.ryibooking_form_viaphone = (By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='usePhone']")
        self.ryibooking_form_viapost = (By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='usePost']")

        # ryi-thankyou
        self.ryithankyou_bikelist = (By.CSS_SELECTOR, "div.thanksPage div.thanksPage__main div.bikeList")
        self.ryithankyou_bikelist_title = (By.CSS_SELECTOR, "div.bikeList__titleBox p.bikeList__title")
        self.ryithankyou_bikelist_list = (By.CSS_SELECTOR, "div.bikeList__out a.bikeList__box")
        self.ryithankyou_cant_decide = (By.CSS_SELECTOR, "div.thanksPage div.thanksPage__main div.thanksPage__decide a")

        # booking
        self.booking_form_email = (By.ID, "email")
        self.booking_submit_button = (By.CSS_SELECTOR, "form div.formModel div.common_sections button.common-cta_btn")

        # ryi-error
        self.errorpage_goback_button = (By.CSS_SELECTOR, "div.errorModel div.errorModel__section a.common-cta_btn")