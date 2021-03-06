from time import sleep

class Processor:
    def __init__(self,
        config,
        scheduler,
        link_generator,
        scraper,
        content_service,
        link_service):
            self.config = config
            self.scheduler = scheduler
            self.link_generator = link_generator
            self.scraper = scraper
            self.content_service = content_service
            self.link_service = link_service
            self.missed = 0

    def process(self):
        if self.config.get_max_missed() < self.missed:
            print('missed max amount ', self.config.get_max_missed())
            return
        sleep(self.scheduler.delay_time())
        link = self._find_link()
        if not link:
           self.process()
        print('processing link ', link)
        content = self.scraper.scrape(link)
        self._process_link(content)
        return self._process_content(content)

    def _process_content(self, content):
        try: 
            return self.content_service.process(content)
        except Exception as e:
            print('Exception occured processing content: ', e)
        except: 
            print('Unexpected error occured')

    def _process_link(self, content):
        try: 
            self.link_service.process(content)
        except Exception as e:
            print('Exception occured processing link: ', e)
        except: 
            print('Unexpected error occured')

    def _find_link(self):
        try:
            return self.link_generator.next()
        except StopIteration:
            self.missed = self.missed + 1
            print('stopped')
