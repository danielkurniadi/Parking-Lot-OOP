require 'spec_helper'

RSpec.describe 'Parking Lot' do
  let(:pty) { PTY.spawn('parking_lot') }

  before(:each) do
    run_command(pty, "create_parking_lot 3\n")
  end

  it "can create a parking lot", :sample => true do
    expect(fetch_stdout(pty)).to end_with("Created a parking lot with 3 slots\n")
  end

  it "can park a car" do
    run_command(pty, "park KA-01-HH-3141 Black\n")
    expect(fetch_stdout(pty)).to end_with("Allocated slot number: 1\n")
  end
  
  it "can unpark a car" do
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "leave 1\n")
    expect(fetch_stdout(pty)).to end_with("Slot number 1 is free\n")
  end
  
  it "can report status" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "status\n")
    expect(fetch_stdout(pty)).to end_with(<<-EOTXT
Slot No.    Registration No    Colour
1           KA-01-HH-1234      White
2           KA-01-HH-3141      Black
3           KA-01-HH-9999      White
EOTXT
)
  end

  it "can query slot number by car registration number" do
    run_command(pty, "park KA-11-HH-8141 Black\n")
    run_command(pty, "slot_number_for_registration_number KA-11-HH-8141\n")
    expect(fetch_stdout(pty)).to end_with("1\n")
  end

  it "can query slot numbers by car color" do
    run_command(pty, "park KA-01-IH-3141 Black\n")
    run_command(pty, "park KA-02-UH-1241 White\n")
    run_command(pty, "park KA-05-HG-2211 White\n")
    run_command(pty, "slot_numbers_for_cars_with_colour White\n")
    expect(fetch_stdout(pty)).to end_with("2, 3\n")
  end

  it "can query registration numbers by car color" do
    run_command(pty, "park KA-01-IH-3141 Black\n")
    run_command(pty, "park KA-02-UH-1241 White\n")
    run_command(pty, "park KA-05-HG-2211 White\n")
    run_command(pty, "registration_numbers_for_cars_with_colour White\n")
    expect(fetch_stdout(pty)).to end_with("KA-02-UH-1241, KA-05-HG-2211\n")
  end
  
  pending "add more specs as needed"
end
