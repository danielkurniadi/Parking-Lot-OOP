# Parking-engine

## Problem Statement
Imagine a one-dimensional parking lot (meaning car slots are arranged in lengthwise).
Each parking space is given a natural index, starting with 0, 1, 2, 3, … to n, where n < inf and n is specified by user (you).
The entire lot is a single row of spaces — so that space 0 is the one closest to the entrance. 
There are a finite number of cars randomly parked in the lot, as people come and go as they wish. 
A new car has just arrived outside the lot, and the driver asks you, “Where is the closest open parking space?”

This OOP problem might be simple, but when we start to think of adding flexibility and extensibility to our parking lot system we might sacrifice some simplicity there. Indeed, no model is right/perfect and this makes the problem interesting. You can build a simple system with 100 lines of python, or you can build it with backend-database-ORM tools and make it scalable for hosting millions of car with flexiblility to adhere any specs. Certainly the later one will use enourmous lines of codes just for this problem but maybe you can sell it! (lol... enough said let's go!).

### Assumption
Before we go...
- One dimensional parking lots, where each car slots are arrange in lengthwise.
- Every vehicle is same of same type and assumed a car. 
- Every car has color and car plate number, thus the plate number is unique for all car.
- Any car can occupy any carslots as long as it's empty.

### Specs
One last thing...
- Initiate/create one parking lot at a time with specified number of carslots.
- New/incoming vehicle is routed to the empty carslots nearest to the entrance gate. If there isn't empty slot, then it cannot park in the lot (not assigned)
- Feature to query car(s) and where they park (indicated by carslot index). Query car(s) by car color and car plate number.  

## Future Improvement
Yes I'm a futurist. Let's talk about future improvement first. What can be improved? Well, what kind of parking lots that shaped as 1-Dimensional (You get the idea hmm)?
Hence we can improve lot of things on:
- Extend to solve problems where parking lots is 2 dimensional (most likely a square/rect spaces) or even 3 dimensional (like a parking storey, it has shape of level x length x width).
- With different parking lots shape described above, we should introduce a new routing logics (e.g. find the closest slot where distance measured by eucledian distance).
- Introduce different vechicle as currently the solution assume everything is a car. Perhaps introduce a vallet parking, motorcycle park, etc.
- Add billing/timer for checkout pay. Hence implement billing system as well.

## Getting Started & Setup
Parking-engine is a solution engineered for parking lot problem. Parking-engine is written in Python3 and has testing suite available in Ruby (functional and spec tests) and Python (unit-tests). 

This project needs [Ruby](https://www.ruby-lang.org/en/documentation/installation/) and [Python](https://www.python.org/), followed by some libraries.

### Ruby
First, install [Ruby](https://www.ruby-lang.org/en/documentation/installation/). Then run the following commands under the `functional_spec` dir.

```
functional_spec $ ruby -v # confirm Ruby present
ruby 2.5.1p57 (2018-03-29 revision 63029) [x86_64-darwin17]
functional_spec $ gem install bundler # install bundler to manage dependencies
Successfully installed bundler-1.16.1
Parsing documentation for bundler-1.16.1
Done installing documentation for bundler after 2 seconds
1 gem installed
functional_spec $ bundle install # install dependencies
...
...
Bundle complete! 3 Gemfile dependencies, 8 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
functional_spec $ 

```

### Python
Running the Parking-engine and its unit-tests is easier using the bash scripts I have provided. The scripts provided will download all necessary Python packages using `pip` and setup Python environment using `.virtualenv`. It will also run all Python unit-tests in the directory. To setup Python virtual environment:
```
parking_lot $ source ./bin/setup  #setup and source virtualenv
. . .
```

## Usage

### Interactive Session

In order to run *interactive input session*, run the `./bin/setup` to ensure that Python environment is setup. Example is shown below:

```
parking_lot $ source ./bin/setup  #setup and source virtualenv
parking_lot $ ./bin/parking_lot
parking_lot $ create_parking_lot 6 #interactive session begin
. . .(output)
```

### Non-interactive Session
In order to run *file-based session*, just add input file path relative to current working directory e.g `Parking-engine/file_input.txt`. Example is shown below:

```
parking_lot $ source ./bin/setup  #setup and source virtualenv
parking_lot $ ./bin/parking_lot Parking-engine/file_input.txt
. . . (output)
```

### Unit-tests (Nose and Pytest)
Running the Python unit-tests is easy when `Nose` testing framework has been installed. 
```
parking_lot $ source ./bin/setup #setup and source virtualenv
parking_lot $ python3 -m nose -w Parking-engine/
. . .
```

### Funtional-tests suite

You can run the full suite from `parking_lot` by doing
```
parking_lot $ bin/run_functional_specs
```

You can run the full suite directly from `parking_lot/functional_spec` by doing
```
parking_lot/functional_spec $ bundle exec rake spec:functional
```

You can run a specific test from `parking_lot/functional_spec` by providing the spec file and tag  for the test. In this example we're running the `can create a parking lot` test which has tag "sample".
```
parking_lot/functional_spec $ PATH=$PATH:../bin bundle exec rspec spec/parking_lot_spec.rb --tag sample
```

## Parking-engine Framework - Base Components

**Session**
Represents a session process that handle the event when user run the parking lot program. `Session` object has `run()` to run the controller and handle user session until parking lot is terminated.

**Controllers**
The inner components of parking lot engine. Controllers connect the user session to a parking lot model which is named `CarSlot`.

**Slots**
Represent structural areas within a parking lot. *Slots* can be regarded as one-dimentional slots for vehicle parking. *Slots* object has flexibility and can be inherited to slots manager object that can be implemented for parking lot with different routing logics for vehicle.

**Vehicle**
Vehicle objects represent one vehicle that take up a slot in the parking lot.


