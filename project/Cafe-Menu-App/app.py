import streamlit as st

# ==============================
# App Title and Description
# ==============================
st.set_page_config(page_title="Streamlit Café", page_icon="☕", layout="wide")
st.title("☕ Streamlit Café Menu")
st.subheader("Discover and order your favorite drinks & snacks!")

# ==============================
# Sidebar Filters
# ==============================
menu_category = st.sidebar.selectbox(
    "Choose category", 
    ["All", "Tea", "Coffee", "Juice", "Snacks"]
)

# ==============================
# Menu Data (static for demo)
# ==============================
menu_items = [
    {"name": "Masala Chai", "price": 25, "category": "Tea", "image": "data/chai.jpeg"},
    {"name": "Cold Coffee", "price": 60, "category": "Coffee", "image": "data/coffee.jpeg"},
    {"name": "Mango Juice", "price": 50, "category": "Juice", "image": "data/juice.jpeg"},
    {"name": "Samosa", "price": 30, "category": "Snacks", "image": "data/snacks.jpeg"},
]

# Filter items
if menu_category != "All":
    menu_items = [item for item in menu_items if item["category"] == menu_category]

# ==============================
# Layout - Display in 2 Columns
# ==============================
col1, col2 = st.columns(2)
cols = [col1, col2]
total = 0

for i, item in enumerate(menu_items):
    with cols[i % 2]:
        st.image(item["image"], use_container_width=True)
        st.markdown(f"### {item['name']}")
        st.markdown(f"💰 Price: ₹{item['price']}")
        qty = st.number_input(f"Select quantity for {item['name']}", min_value=0, max_value=5, key=item['name'])
        total += qty * item["price"]

# ==============================
# Order Summary
# ==============================
st.markdown("---")
st.header("🧾 Order Summary")
if total > 0:
    st.success(f"Your total order amount is **₹{total}**")
else:
    st.info("Select some items to see your total order amount.")
