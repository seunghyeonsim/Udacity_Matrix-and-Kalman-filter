# Udacity_Matrix-and-Kalman-filter
Kalman Filter and your Matrix Class
Once you have a working matrix class, you can use the class to run a Kalman filter!

You will need to put your matrix class into the workspace:

Click above on the "JUPYTER" logo.
Then open the matrix.py file, and copy in your code there.
Make sure to save the matrix.py file.
Then click again on the "JUPYTER" logo and open this file again.
You can also download this file kalman_filter_demo.ipynb and run the demo locally on your own computer.

Once you have our matrix class loaded, you are ready to go through the demo. Read through this file and run each cell one by one. You do not need to write any code in this Ipython notebook.

The demonstration has two different sections. The first section creates simulated data. The second section runs a Kalman filter on the data and visualizes the results.

Kalman Filters - Why are they useful?
Kalman filters are really good at taking noisy sensor data and smoothing out the data to make more accurate predictions. For autonomous vehicles, Kalman filters can be used in object tracking.

Kalman Filters and Sensors
Object tracking is often done with radar and lidar sensors placed around the vehicle. A radar sensor can directly measure the distance and velocity of objects moving around the vehicle. A lidar sensor only measures distance.

Put aside a Kalman filter for a minute and think about how you could use lidar data to track an object. Let's say there is a bicyclist riding around in front of you. You send out a lidar signal and receive the signal back. The lidar sensor tells you that the bicycle is 10 meters directly ahead of you but gives you no velocity information.

By the time your lidar device sends out another signal, maybe 0.05 seconds will have passed. But during those 0.05 seconds, your vehicle still needs to keep track of the bicycle. So your vehicle will predict where it thinks the bycicle will be. But your vehicle has no bicycle velocity information.

After 0.05 seconds, the lidar device sends out and receives another signal. This time, the bicycle is 9.95 meters ahead of you. Now you know that the bicycle is traveling -1 meter per second towards you. For the next 0.05 seconds, your vehicle will assume the bicycle is traveling -1 m/s towards you. Then another lidar signal goes out and comes back, and you can update the position and velocity again.

Sensor Noise
Unfortunately, lidar and radar signals are noisy. In other words, they are somewhat inacurrate. A Kalman filter helps to smooth out the noise so that you get a better fix on the bicycle's true position and velocity.

A Kalman filter does this by weighing the uncertainty in your belief about the location versus the uncertainty in the lidar or radar measurement. If your belief is very uncertain, the Kalman filter gives more weight to the sensor. If the sensor measurement has more uncertainty, your belief about the location gets more weight than the sensor mearuement.
