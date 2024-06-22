from factory.autofactory import AutoFactory

car_fac = AutoFactory()

for carname in ['ChevyVolt']:
    car = car_fac.create_instance(carname)
    car.start()
    car.stop()
