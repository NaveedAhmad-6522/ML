'''import numpy as np
companies=["Tesla","Apple","Google"]
indecis=[0,1,2]
zipping=list(zip(companies,indecis))
np.random.seed(42)
stockvalues=np.random.randint(60,90,30)
reshaped=stockvalues.reshape(10,3)
heighst_stock_daily=np.max(reshaped,axis=1)
indice_heighst_Stock_daily=np.argmax(reshaped,axis=1)
heighst_stock_company=np.max(reshaped,axis=0)
Lowest_stock_company=np.min(reshaped,axis=0)
AveragePrice=np.mean(reshaped,axis=0)

'''


import numpy as np

# Step 1: Setup
np.random.seed(42)
companies = np.array(["Tesla", "Apple", "Google"])
stockvalues = np.random.randint(60, 90, 30)
reshaped = stockvalues.reshape(10, 3)  # 10 days × 3 companies

print("📊 Stock Prices (10 days × 3 companies):\n", reshaped)

# Step 2: Company-wise stats
highest_stock_company = np.max(reshaped, axis=0)
lowest_stock_company = np.min(reshaped, axis=0)
average_price_company = np.mean(reshaped, axis=0)

print("\n🏢 Company-wise Highest Stock Prices:", dict(zip(companies, highest_stock_company)))
print("🏢 Company-wise Lowest Stock Prices:", dict(zip(companies, lowest_stock_company)))
print("🏢 Company-wise Average Prices:", dict(zip(companies, np.round(average_price_company, 2))))

# Step 3: Daily analysis
highest_daily_index = np.argmax(reshaped, axis=1)
print("\n📅 Highest Stock Company Per Day:")
for day, idx in enumerate(highest_daily_index):
    print(f"  Day {day+1}: {companies[idx]} with price {reshaped[day][idx]}")

# Step 4: Count how many times Tesla was top
tesla_top_days = np.sum(highest_daily_index == 0)
print(f"\n🚀 Tesla had the highest stock on {tesla_top_days} days.")

# Step 5: Normalization
min_vals = reshaped.min(axis=0)
max_vals = reshaped.max(axis=0)
normalized = (reshaped - min_vals) / (max_vals - min_vals)

print("\n🧮 Normalized Stock Prices (0 to 1 range):")
print(np.round(normalized, 2))

# Step 6: Day-to-day Tesla price difference
tesla_prices = reshaped[:, 0]
tesla_diff = np.diff(tesla_prices)
biggest_jump_day = np.argmax(np.abs(tesla_diff))
print(f"\n📈 Tesla had the biggest jump from Day {biggest_jump_day+1} to Day {biggest_jump_day+2}")
print("Day-wise Tesla price changes:", tesla_diff)


