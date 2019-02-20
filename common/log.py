import logging, time


class log(object):
    def __init__(self):
        self.path = './test_Result/Test_logs/'
        self.now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        self.filename = '-Tests_log.log'
        #self.filename = '-Tests_log.log'
        logging.basicConfig(level=logging.INFO,
                                 format='%(asctime)s wLog: %(levelname)s [** %(message)s **]',
                                 datefmt='%Y-%m-%d %H:%M:%S',
                                 filename=self.path + self.now + self.filename,
                                 filemode='w')
    def wlog(self,log):
        logging.info(log)
    
