""" plots and polynomial features"""
import numpy as np
import matplotlib.pyplot as plt


class PolynomialTransformer:
    def transform(self, speed_df):
        result = speed_df.copy()
        if not np.isfinite(result[['speed', 'fuel_use']].to_numpy()).all():
            raise ValueError('Features and target must be finite.')
        result['speed_sq'] = result['speed'] ** 2
        return result


class VehicleEDA:
    def raw_scatter(self, analysis_df):
        fig, ax = plt.subplots(figsize=(10, 5.5), constrained_layout=True)
        ax.scatter(analysis_df['Vehicle Speed[km/h]'], analysis_df['Fuel Use[L/100km]'],
                   s=4, alpha=0.035, color='#237a9b', edgecolors='none', rasterized=True)
        ax.set(title=f'Vehicle 531: raw moving readings (n={len(analysis_df):,}, speed ≥ 10 km/h)',
               xlabel='Vehicle speed (km/h)', ylabel='Estimated fuel use (L/100 km)')
        ax.grid(alpha=0.2)
        ax.set_axisbelow(True)
        return fig, ax

    def speed_scatter(self, speed_df):
        fig, ax = plt.subplots(figsize=(10, 5.5), constrained_layout=True)
        points = ax.scatter(speed_df['speed'], speed_df['fuel_use'],
                            c=speed_df['n_readings'], cmap='viridis', s=40)
        fig.colorbar(points, ax=ax, label='Number of source readings')
        ax.set(title=f'Vehicle 531: {len(speed_df)} speed-level averages (unfitted)',
               xlabel='Mean speed in rounded-speed group (km/h)',
               ylabel='Estimated fuel use (L/100 km)')
        ax.grid(alpha=0.2)
        ax.set_axisbelow(True)
        return fig, ax
