

class Util(object):

    def tap_coordinate(self,x,y):
        x_ratio=x/1080
        y_ratio=y/2076
        screen_size = self.driver.driver.get_window_size()
        width = screen_size.get('width')
        height = screen_size.get('height')
        self.driver.driver.tap([(round(width * x_ratio), round(height * y_ratio))],100)


