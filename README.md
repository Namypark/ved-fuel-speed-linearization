# Fuel Use vs Speed: Polynomial Linearization

Foundations of Machine Learning, Week 4 lab. We model fuel use against vehicle speed with a
quadratic fitted by ordinary linear regression:

```
fuel_use = w2 · speed² + w1 · speed + b
```

## Data

Source: [Vehicle Energy Dataset (VED)](https://github.com/gsoh/VED). G. Oh, D. J. LeBlanc,
H. Peng, "Vehicle Energy Dataset (VED), A Large-scale Dataset for Vehicle Energy Consumption
Research", IEEE T-ITS, 2020.

`data/ved_vehicle531.csv` contains 381,876 records from 478 trips of vehicle 531, a gasoline
car with a 1.5 L 4-cylinder engine.

| Column | Meaning |
|---|---|
| `DayNum` | Days since 1 Nov 2017 |
| `VehId`, `Trip` | Vehicle and trip IDs |
| `Timestamp(ms)` | Time since the start of the trip |
| `Vehicle Speed[km/h]` | Speed |
| `MAF[g/sec]` | Mass air flow into the engine |

VED does not log fuel rate for this vehicle. We derive it from air flow, using gasoline's
stoichiometric air-fuel ratio (14.7) and density (745 g/L):

```
Fuel Rate [L/hr]     = MAF × 3600 / (14.7 × 745)
Fuel Use [L/100km]   = Fuel Rate / Speed × 100
```

`data/ved_vehicle119_trip985.csv` is the original single-trip extract (vehicle 119), kept for
reference.

### Rebuilding the data

1. Download `VED_DynamicData_Part1.7z` and `VED_DynamicData_Part2.7z` from the VED repo's
   `Data/` folder.
2. Extract both into one folder.
3. Run `uv run python src/extract_ved.py --src path/to/that/folder`.

## Setup

```
uv sync
```

Then open `src/main.ipynb` and pick the `.venv` kernel. It is one notebook, run top to bottom:

- Part 1: data setup and cleaning (Nnamdi)
- Part 2: plots and the `speed_sq` feature (Rangeetha)
- Part 3: the quadratic fitted with `np.linalg.lstsq` (Davis)
- Part 4: scikit-learn fit and model checking (Carlos)

Keep notebooks in `src/` so `from data_loader import DataLoader` works. Load the data with:

```python
from data_loader import DataLoader
df = DataLoader().load()
```

## Team

| Member | Part |
|---|---|
| Nnamdi | Data setup + project integration |
| Rangeetha | Transformation + exploratory analysis |
| Davis | NumPy model |
| Carlos | scikit-learn + model checking |
