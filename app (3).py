import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# App Title and Description
# --------------------------------------------------
st.title("Exponential Speed Model")
st.subheader("Interactive Algebra 2 Exponential Growth & Decay")

st.markdown(
    """
    This app models how a car's speed changes over time using an **exponential equation**.

    Students can adjust the **initial speed**, **rate of change**, and **time** to explore
    exponential **growth** and **decay**.
    """
)

# --------------------------------------------------
# Sidebar Controls
# --------------------------------------------------
st.sidebar.header("Model Parameters")

# Initial speed (mph)
initial_speed = st.sidebar.slider(
    "Initial Speed (mph)", 30, 120, 90, 5
)

# Rate of change (% per hour)
rate_percent = st.sidebar.slider(
    "Rate of Change (% per hour)", -20, 20, 8, 1
)

# Convert percent to decimal
rate = rate_percent / 100

# Time (hours)
time_hours = st.sidebar.slider(
    "Time (hours)", 0, 24, 2, 1
)

# --------------------------------------------------
# Exponential Model Function
# --------------------------------------------------
# S(t) = S0 * (1 + r)^t

def speed_model(t, s0, r):
    return s0 * (1 + r) ** t

# Time values for graph
t = np.linspace(0, time_hours, 100)

# Calculate speeds
speeds = speed_model(t, initial_speed, rate)
final_speed = speed_model(time_hours, initial_speed, rate)

# --------------------------------------------------
# Display Numerical Result
# --------------------------------------------------
st.markdown("### Result")
st.write(
    f"After **{time_hours} hours**, the car's speed is approximately "
    f"**{final_speed:.2f} mph**."
)

# --------------------------------------------------
# Graph
# --------------------------------------------------
fig, ax = plt.subplots()
ax.plot(t, speeds)
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Speed (mph)")
ax.set_title("Speed vs. Time (Exponential Model)")

st.pyplot(fig)

# --------------------------------------------------
# Interpretation
# --------------------------------------------------
st.markdown("### Interpretation")

if rate > 0:
    st.write("- The speed is increasing exponentially (growth).")
elif rate < 0:
    st.write("- The speed is decreasing exponentially (decay).")
else:
    st.write("- The speed remains constant.")

# --------------------------------------------------
# Model Limitations
# --------------------------------------------------
st.markdown("### Model Limitations")
st.warning(
    "This model is theoretical and not realistic for real driving conditions. "
    "It is intended for educational purposes only."
)
