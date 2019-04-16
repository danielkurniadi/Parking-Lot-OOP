# Parking-engine

Parking-engine is a solution engineered for parking lot problem. Parking-engine is written in Python3 and has testing suite available in Ruby (functional and spec tests) and Python (unit-tests). 

This project needs [Ruby](https://www.ruby-lang.org/en/documentation/installation/) and [Python](https://www.python.org/), followed by some libraries.

## Setup
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




