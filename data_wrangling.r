library(tidyverse)
library(tidymodels)

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
