import logging
import unittest

#file_log = logging.FileHandler("runner_tests.log")
    #console_out = logging.StreamHandler()
logging.basicConfig(level=logging.INFO, filename="runner_tests.log", filemode="w",
                    encoding="utf-8", format="%(asctime)s / %(levelname)s / %(message)s")

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

#first = Runner('Вася', 10)
#second = Runner('Илья', 5)
#third = Runner('Арсен', 10)
#
#t = Tournament(101, first, second)
#print(t.start())

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False,"Тесты в этом кейсе замороженны")
    def test_walk(self):
        try:
            runner1 = Runner("Runner",speed = -5)
            logging.info(f"test_walk выполнен успешно")
            for i in range (10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
        except ValueError:
            logging.warning(f"Неверная скорость Runner")

    @unittest.skipIf(False, "Тесты в этом кейсе замороженны")
    def test_run(self):
        try:
            runner2 = Runner("Runner")
            logging.info(f"test_run выполнен успешно")
            for i in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
        except TypeError:
            logging.warning(f"Неверный тип данных для объекта Runner")

    @unittest.skipIf(False, "Тесты в этом кейсе замороженны")
    def test_challenge(self):
        runner = Runner("a")
        runner = Runner("b")
        for i in range(10):
            runner.run()
        for i in range(10):
            runner.walk()
        self.assertNotEqual(runner.distance, 100)
        self.assertNotEqual(runner.distance, 50)

if __name__ == "__main__":
    unittest.main()

