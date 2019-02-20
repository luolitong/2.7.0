from pages import product_prelogin
from pages import product_person_info
import configparser

if __name__=='__main__':
    # pd=product_prelogin.ProductDetail()
    # pd.from_msg_button()
    # pp=product_person_info.ProductPersonInfo()
    # pp.change_email_address('luolitong@$#@#$!',False)
    con=configparser.ConfigParser()
    con.read('panda-config.txt')
