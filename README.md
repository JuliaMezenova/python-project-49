### Hexlet tests and linter status:
[![Actions Status](https://github.com/JuliaMezenova/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/JuliaMezenova/python-project-49/actions)
<a href="https://codeclimate.com/github/JuliaMezenova/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/60ec1ecaeff526bb716e/maintainability" /></a>
# Проект "Игры разума".
Проект Brain-games содержит в себе пять консольных игр, связанных с числами. Для того чтобы начать играть, выберите какую-либо игру, набрав в командной строке одноименную команду.
1. Brain-even. В этой игре пользователь, после того,как введет свое имя, должен ответить "да"или "нет" на вопрос и четности появившегося числа. Если пользователь три раза введет верный ответ - игра выйграна. Если ответ ошибочный - игра окончена поражением пользователя.

2. Brain-calc. В этой игре нужно посчитать результат появившегося выражения и ввести ответ. Принцип проигрыша-выйгрыша тот же, что и в предыдущей игре.

3. Brain-gcd. В данной  игре необходимо ввести наибольший общий делитель для двух появившихся чисел.

4. Brain-progression. Здесь необходимо ввести пропущенное число в появившейся арифметической прогрессии.

5. Brain-prime. В этой игре нужно ответить "да", если число простое (то есть делится только на себя и на единицу),и "нет" - если число не простое.

## Установка игры.
Для установки игры склонируйте репозиторий к себе в систему командой git clone git@github.com:JuliaMezenova/python-project-49.git 

Затем проделайте следующие команды:
1. poetry install
2. poetry build
3. poetry publish
4. python3 -m pip install --upgrade --force-reinstall dist/hexlet_code-0.1.2-py3-none-any.whl

## Демонстрационное видео по установке и работе игр.

* Asciinema: Запись игры Brain-even  [![asciicast](https://asciinema.org/a/REsMCpf3oyTbVfENc6LkHudiT.svg)]
* Asciinema: Запись игры Brain-calc  [![asciicast](https://asciinema.org/a/q7b4gH0fOEwqqTd8b7VhINKoU.svg)]
* Asciinema: Запись игры Brain-gcd  [![asciicast](https://asciinema.org/a/RR2r14DRPgC8qcJTY2ug0oInV.svg)]
Asciinema: Запись игры Brain-progression  [![asciicast](https://asciinema.org/a/M83dlhfi1sI3RntIQOke6jpFx.svg)]
Asciinema: Запись игры Brain-prime   [![asciicast](https://asciinema.org/a/9znKIMcvE0TpFiyzZMcmRi4f1.svg)]
Asciinema: Запись установки игры и примеры работы всех пяти игр Brain-games [![asciicast](https://asciinema.org/a/vrjGFbHAAUWhM1fd0v2ZEvVTS.svg)]
=======
