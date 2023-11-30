library(tidyverse)
library(tidymodels)
library(patchwork)

theme_set(theme_bw())

data <- read_csv("data/chronic_kidney_disease.csv")

print(head(data))

tidy_data <- data |>
  mutate(age = as.numeric(age),
         blood_pressure = as.numeric(blood_pressure),
         specific_gravity = as.numeric(specific_gravity),
         albumin = as.numeric(albumin),
         sugar = as.numeric(sugar),
         blood_glucose_random = as.numeric(blood_glucose_random),
         blood_urea = as.numeric(blood_urea),
         serum_creatinine = as.numeric(serum_creatinine),
         sodium = as.numeric(sodium),
         potassium = as.numeric(potassium),
         haemoglobin = as.numeric(haemoglobin),
         packed_cell_volume = as.numeric(packed_cell_volume),
         white_blood_cell_count = as.numeric(white_blood_cell_count),
         red_blood_cell_count = as.numeric(red_blood_cell_count))

print(head(tidy_data))

write_csv(tidy_data, 'data/ckd_clean.csv')

density_age <- ggplot(tidy_data, aes(x = age)) +
  geom_density() +
  labs(x = "Age")

density_bp <- ggplot(tidy_data, aes(x = blood_pressure)) +
  geom_density() +
  labs(x = "Blood Pressure (mm/Hg)")

density_sg <- ggplot(tidy_data, aes(x = specific_gravity)) +
  geom_density() +
  labs(x = "Specific Gravity")

density_albumin <- ggplot(tidy_data, aes(x = albumin)) +
  geom_density() +
  labs(x = "Albumin")

density_sugar <- ggplot(tidy_data, aes(x = sugar)) +
  geom_density() +
  labs(x = "Sugar")

density_bgr <- ggplot(tidy_data, aes(x = blood_glucose_random)) +
  geom_density() +
  labs(x = "Blood Glucose Random (mgs/dl)")

density_bu <- ggplot(tidy_data, aes(x = blood_urea)) +
  geom_density() +
  labs(x = "Blood Urea (mgs/dl)")

density_sc <- ggplot(tidy_data, aes(x = serum_creatinine)) +
  geom_density() +
  labs(x = "Serum Creatinine (mgs/dl)")

density_sodium <- ggplot(tidy_data, aes(x = sodium)) +
  geom_density() +
  labs(x = "Sodium (mEq/L)")

density_pt <- ggplot(tidy_data, aes(x = potassium)) +
  geom_density() +
  labs(x = "Potassium (mEq/L)")

density_hg <- ggplot(tidy_data, aes(x = haemoglobin)) +
  geom_density() +
  labs(x = "Hemoglobin (gms)")

density_pcv <- ggplot(tidy_data, aes(x = packed_cell_volume)) +
  geom_density()

density_wbcc <- ggplot(tidy_data, aes(x = white_blood_cell_count)) +
  geom_density() +
  labs(x = "White Blood Cell Count (cells/cumm)")

density_rbcc <- ggplot(tidy_data, aes(x = red_blood_cell_count)) +
  geom_density() +
  labs(x = "Red Blood Cell Count (millions/cumm)")

(density_age + density_bp) / (density_sg + density_albumin)
(density_sugar + density_bgr) / (density_bu / density_sc)
(density_sodium + density_pt) / (density_hg / density_pcv)
density_wbcc / density_rbcc
