# IOT Class

Contains all projects and code labs and homework of this course.

## Code Explanation

### iot_pr.py

This Python code connects to a Firebase Realtime Database, simulates the collection of temperature sensor data, processes this data to detect anomalies, and takes action if temperatures outside the normal range (0.0 °C to 35.0 °C) are detected.

Here’s a breakdown of what each part of the code does:

    - Firebase Connection: Connects to a Firebase database using specific credentials.
    - Data Collection: Retrieves the last 3 temperature records from Firebase.
    - Anomaly Detection: Checks if the temperature is outside the normal range (below 0.0 °C or above 35.0 °C).
    - Action: Prints an alert in red if an anomaly is detected.
    - Loop: Repeats the process every 30 seconds.

### publisher and subscriber MQTT scripts

This code demonstrates how to publish and subscribe to MQTT topics.

Publisher: Connects to an MQTT broker and continuously publishes random temperature (20.0°C to 25.0°C) and humidity (30% to 60%) data to specific topics every 5 seconds.
Subscriber: Connects to the same MQTT broker, subscribes to the temperature and humidity topics, and prints the received data.
Both parts involve setting up a client, connecting to the broker, and handling either data publishing or receiving.

### Computing Levels

This code simulates an IoT architecture with Edge, Fog, Roof, and Cloud Computing:

    Edge Devices: Five simulated IoT devices generate temperature and humidity data, stored in dataframes.
    Fog Node: Aggregates data from all devices, calculating average temperature and humidity.
    Roof Node: Further aggregates data from the Fog Node, computing overall averages.
    Cloud Processing: Prints the processed data, simulating advanced processing and storage in the cloud.
    
The entire process is executed sequentially within the main_simulation function.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Example 1](https://www.example.com)
- [Example 2](https://www.example.com)

### Installing

A step by step series of examples that tell you how to get a development
environment running

Say what the step will be

    Give the example

And repeat

    until finished

End with an example of getting some data out of the system or using it
for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Sample Tests

Explain what these tests test and why

    Give an example

### Style test

Checks if the best practices and the right coding style has been used.

    Give an example

## Deployment

Add additional notes to deploy this on a live system

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

  - **Billie Thompson** - *Provided README Template* -
    [PurpleBooth](https://github.com/PurpleBooth)

See also the list of
[contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors)
who participated in this project.

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

  - Hat tip to anyone whose code is used
  - Inspiration
  - etc
