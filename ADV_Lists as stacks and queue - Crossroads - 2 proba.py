'''*Crossroads
Our favorite super-spy action hero Sam is back from his mission in the previous exam, and he has finally found some time to go on a holiday.
He is taking his wife somewhere nice and they're going to have a really good time, but first, they have to get there. Even on his holiday trip,
Sam is still going to run into some problems and the first one is, of course, getting to the airport. Right now, he is stuck in a traffic jam at
a very active crossroads where a lot of accidents happen.
Your job is to keep track of traffic at the crossroads and report whether a crash happened or everyone passed the crossroads safely and our hero
is one step closer to a much desired vacation.
The road Sam is on, has a single lane where cars queue up until the light goes green. When it does, they start passing one by one during
the green light and the free window before the intersecting road's light goes green. During one second only one part of a car (a single character)
passes the crossroads. If a car is still in the crossroads when the free window ends, it will get hit at the first character that is still in
the crossroads.

Input

On the first line, you will receive the duration of the green light in seconds – an integer in the range [1-100]
On the second line, you will receive the duration of the free window in seconds – an integer in the range [0-100]
On the following lines, until you receive the "END" command, you will receive one of two things:

A car – a string containing the model of the car, or
The command "green" which indicates the start of a green light cycle
A green light cycle goes as follows:
During the green light cars will enter and exit the crossroads one by one
During the free window cars will only exit the crossroads

Output
If a crash happens, end the program and print:
"A crash happened!"
"{car} was hit at {characterHit}."

If everything goes smoothly and you receive an "END" command, print:
"Everyone is safe."
"{totalCarsPassed} total cars passed the crossroads."

Constraints
The input will be within the constaints specified above and will always be valid. There is no need to check it explicitly.

Examples
Input
Output
Comments

10
5
Mercedes
green
Mercedes
BMW
Skoda
green
END

Everyone is safe.

3 total cars passed the crossroads.

During the first green light (10 seconds), the Mercedes (8) passes safely.
During the second green light, the Mercedes (8) passes safely and there are 2 seconds left.
The BMW enters the crossroads and when the green light ends, it still has 1 part inside ('W'), but has 5 seconds to leave and passes successfully.
The Skoda never enters the crossroads, so 3 cars passed successfully.

9
3
Mercedes
Hummer
green
Hummer
Mercedes
green
END

A crash happened!

Hummer was hit at e.

Mercedes (8) passes successfully and Hummer (6) enters the crossroads but only the 'H' passes during the green light.
There are 3 seconds of free window, so "umm" passes and the Hummer gets hit at 'e' and the program ends with a crash.


50
5
Toyota
Toyota
Toyota
Toyota
Toyota
Toyota
Toyota
Toyota
Toyota
Toyota
green
END


'''


green_light = int(input())
free_window = int(input())


#from collections import deque
cars = []
crash = 0
car = ''
passed = 0

while True:

    command = input()

    if command == 'END' or crash == 1:
        break
    elif command != 'green':
        cars.append(command)

    elif command == 'green':
        green = green_light
        free = free_window


        while green and free:

            if cars:                        # if there are still cars
                car = cars[0]               # car enters
            else:

                break

            if len(car) and len(car) <= green:           # if the green is longer than car
                green = green - len(car)
                if cars:
                  cars.pop(0)
                  passed +=1
                  car = ''
                else:
                    passed +=1
                    break
            elif len(car) and len(car) > green:            # if green is shorter than car
                car_part = len(car) - green
                car = car[green:]
                green = 0
                if len(car) <= free:        # starts the free window. check the car if it can go out during free window
                    passed+=1
                    if cars:                # if there are still cars waiting
                        cars.pop(0)
                    else:
                        break
                else:                       # if the car cannot go out - CRASH!
                    crash = 1
                    car = car[free-1:]
                    print(f"A crash happened!\n{cars[0]} was hit at {car[1]}.")
                    break


if crash == 0:
   print(f"Everyone is safe.\n{passed} total cars passed the crossroads.")

