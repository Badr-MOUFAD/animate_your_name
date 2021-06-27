import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.core.fromnumeric import repeat


class AnimatedWave:
    # params
    # time in ms
    def __init__(self, fig, ax, spatial_period, wave_amplitude=1, time_period=5000, interval=200, nb_spatial_periods=1, nb_points=100):
        # store params
        # figure
        self.fig = fig
        self.ax = ax
        # periods
        self.spatial_period = spatial_period
        self.time_period = time_period
        # duration between frames
        self.interval = interval
        
        self.nb_spatial_periods = nb_spatial_periods
        self.nb_points = nb_points

        # wave params
        self.delta = self.nb_spatial_periods * self.spatial_period / self.nb_points
        self.k = 2 * np.pi * self.delta / self.spatial_period

        self.nb_time_points = (5 / self.spatial_period - 1/2) * self.time_period / self.interval
        self.omega = 2 * np.pi * self.interval / self.time_period

        self.wave_xpoints = np.array(
            [self.delta * i for i in range(self.nb_points)], 
            dtype=float
            )

        # define plot
        self.cos_plot, = ax.plot([], [], markerfacecolor='None', color="#1f77b4", marker="o", linestyle='None')

        return

    def render(self, frame):
        current_period = self.frame_to_period(frame)
        select_index =  int((current_period + 1) * self.nb_points / (self.spatial_period * self.nb_spatial_periods))

        new_cos = np.array(
            [np.cos(self.k * i - self.omega * frame - 2 * np.pi / self.spatial_period) 
            for i in range(self.nb_points)], 
            dtype=float
        )
        self.cos_plot.set_data(self.wave_xpoints[:select_index], new_cos[:select_index])

        return self.cos_plot

    def animate_wave(self):

        def anime(frame):
            current_period = self.frame_to_period(frame)

            select_index =  int((current_period + 1) * self.nb_points / (self.spatial_period * self.nb_spatial_periods))

            new_cos = np.array(
                [np.cos(self.k * i - self.omega * frame - 2*np.pi/self.spatial_period) for i in range(self.nb_points)][:select_index], 
                dtype=float
            )
            self.cos_plot.set_data(self.wave_xpoints[:select_index], new_cos)

            return self.cos_plot


        self.a = FuncAnimation(
            self.fig, anime, 
            frames=range(int(self.nb_time_points) * self.spatial_period), 
            interval=self.interval, repeat=False
            )

        return

    def frame_to_period(self, current_frame):
        return int(current_frame / self.nb_time_points)


# # example
# fig, ax = plt.subplots()

# # ax limits
# ax.set_xlim([-1, 5 * 2])
# ax.set_ylim([-1.25, 1.25])

# wave = AnimatedWave(fig, ax, spatial_period=5, nb_points=30)

# wave.animate_wave()

# plt.show()
