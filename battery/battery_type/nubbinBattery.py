from battery.battery import Battery


class NubbinBattery(Battery):
    def __int__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date


    def needs_service(self):
        date_for_service = self.last_service_date.replace(year = self.last_service_date.year + 4)

        if self.current_date > date_for_service:
            return True
        else:
            return False

