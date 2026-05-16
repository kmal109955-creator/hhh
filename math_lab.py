import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from sympy import *
import sympy as sp
import math
import random
from fractions import Fraction

# Page configuration
st.set_page_config(
    page_title="Math Lab | مختبر الرياضيات",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', 'Cairo', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    }

    .tool-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        transition: transform 0.2s;
    }

    .tool-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    }

    .result-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #667eea;
        margin-top: 1rem;
    }

    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }

    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        text-align: center;
    }

    .sidebar-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🔬 Math Lab | مختبر الرياضيات</h1>
    <p>Your Interactive Mathematics Workspace | مساحتك التفاعلية للرياضيات</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown('<div class="sidebar-title">🧮 الأدوات | Tools</div>', unsafe_allow_html=True)
tool = st.sidebar.radio("", [
    "📊 Advanced Calculator",
    "📈 Function Plotter", 
    "➗ Equation Solver",
    "📐 Trigonometry Lab",
    "📉 Statistics Studio",
    "🔢 Matrix Operations",
    "💱 Unit Converter",
    "🎲 Probability & Combinatorics",
    "📏 Geometry Tools",
    "🔍 Number Theory"
])

# Initialize session state for calculator history
if 'calc_history' not in st.session_state:
    st.session_state.calc_history = []

# ============================================
# 1. ADVANCED CALCULATOR
# ============================================
if tool == "📊 Advanced Calculator":
    st.header("📊 Advanced Scientific Calculator")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Expression Evaluator")
        expr = st.text_input("Enter expression (e.g., sin(pi/4) + sqrt(16) * log(100)):", 
                            value="sin(pi/4) + sqrt(16)")

        if st.button("Calculate", key="calc_btn"):
            try:
                # Safe evaluation with math functions
                safe_dict = {
                    'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                    'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
                    'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
                    'sqrt': math.sqrt, 'log': math.log, 'log10': math.log10,
                    'exp': math.exp, 'abs': abs, 'pi': math.pi, 'e': math.e,
                    'factorial': math.factorial, 'degrees': math.degrees,
                    'radians': math.radians, 'floor': math.floor, 'ceil': math.ceil,
                    'pow': pow, 'round': round
                }
                result = eval(expr, {"__builtins__": {}}, safe_dict)
                st.markdown(f"""
                <div class="result-box">
                    <h3 style="color: #667eea; margin:0;">Result</h3>
                    <h2 style="margin:0.5rem 0;">{result}</h2>
                    <p style="color: #666; margin:0;">Exact: {Fraction(result).limit_denominator(1000) if isinstance(result, float) else result}</p>
                </div>
                """, unsafe_allow_html=True)
                st.session_state.calc_history.append(f"{expr} = {result}")
            except Exception as e:
                st.error(f"Error: {e}")

        # History
        if st.session_state.calc_history:
            with st.expander("📜 Calculation History"):
                for h in reversed(st.session_state.calc_history[-10:]):
                    st.code(h)

    with col2:
        st.subheader("Quick Functions")
        func = st.selectbox("Function", ["Square Root", "Power", "Logarithm", "Factorial", "GCD", "LCM"])

        if func == "Square Root":
            n = st.number_input("Number", value=16.0)
            if st.button("Compute"):
                st.success(f"√{n} = {math.sqrt(n)}")
        elif func == "Power":
            base = st.number_input("Base", value=2.0)
            exp = st.number_input("Exponent", value=3.0)
            if st.button("Compute"):
                st.success(f"{base}^{exp} = {pow(base, exp)}")
        elif func == "Logarithm":
            n = st.number_input("Number", value=100.0)
            base = st.number_input("Base (e for natural)", value=10.0)
            if st.button("Compute"):
                if base == math.e:
                    st.success(f"ln({n}) = {math.log(n)}")
                else:
                    st.success(f"log_{base}({n}) = {math.log(n, base)}")
        elif func == "Factorial":
            n = st.number_input("Integer", value=5, min_value=0, max_value=170, step=1)
            if st.button("Compute"):
                st.success(f"{n}! = {math.factorial(n)}")
        elif func == "GCD":
            a = st.number_input("A", value=48, step=1)
            b = st.number_input("B", value=18, step=1)
            if st.button("Compute"):
                st.success(f"GCD({a}, {b}) = {math.gcd(int(a), int(b))}")
        elif func == "LCM":
            a = st.number_input("A", value=4, step=1)
            b = st.number_input("B", value=6, step=1)
            if st.button("Compute"):
                gcd = math.gcd(int(a), int(b))
                lcm = abs(int(a) * int(b)) // gcd
                st.success(f"LCM({a}, {b}) = {lcm}")

# ============================================
# 2. FUNCTION PLOTTER
# ============================================
elif tool == "📈 Function Plotter":
    st.header("📈 Interactive Function Plotter")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.subheader("Settings")
        func_input = st.text_input("f(x) =", value="sin(x)")
        x_min = st.number_input("X min", value=-10.0)
        x_max = st.number_input("X max", value=10.0)
        num_points = st.slider("Points", 100, 5000, 1000)

        plot_type = st.selectbox("Plot Type", ["Line", "Scatter", "Area", "Bar"])
        color = st.color_picker("Color", "#667eea")
        show_grid = st.checkbox("Grid", True)
        show_derivative = st.checkbox("Show Derivative", False)

        # Second function option
        add_second = st.checkbox("Add Second Function")
        func2 = None
        if add_second:
            func2 = st.text_input("g(x) =", value="cos(x)")
            color2 = st.color_picker("Color 2", "#e74c3c")

    with col2:
        try:
            x = np.linspace(x_min, x_max, num_points)

            # Safe evaluation
            safe_dict = {'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                        'sqrt': np.sqrt, 'exp': np.exp, 'log': np.log,
                        'abs': np.abs, 'pi': np.pi, 'e': np.e,
                        'sinh': np.sinh, 'cosh': np.cosh, 'tanh': np.tanh,
                        'arcsin': np.arcsin, 'arccos': np.arccos, 'arctan': np.arctan}

            y = eval(func_input, {"__builtins__": {}, "x": x, "np": np}, safe_dict)

            fig = go.Figure()

            if plot_type == "Line":
                fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'f(x)={func_input}',
                                        line=dict(color=color, width=3)))
            elif plot_type == "Scatter":
                fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name=f'f(x)={func_input}',
                                        marker=dict(color=color, size=4)))
            elif plot_type == "Area":
                fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', name=f'f(x)={func_input}',
                                        line=dict(color=color)))
            elif plot_type == "Bar":
                fig.add_trace(go.Bar(x=x[::50], y=y[::50], name=f'f(x)={func_input}',
                                    marker_color=color))

            if show_derivative:
                dy = np.gradient(y, x)
                fig.add_trace(go.Scatter(x=x, y=dy, mode='lines', name="f'(x)",
                                        line=dict(color='orange', width=2, dash='dash')))

            if add_second and func2:
                y2 = eval(func2, {"__builtins__": {}, "x": x, "np": np}, safe_dict)
                fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name=f'g(x)={func2}',
                                        line=dict(color=color2, width=3)))

            fig.update_layout(
                title=f"Plot of {func_input}",
                xaxis_title="x",
                yaxis_title="y",
                template="plotly_white",
                showlegend=True,
                height=600
            )

            if show_grid:
                fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
                fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

            st.plotly_chart(fig, use_container_width=True)

            # Statistics
            st.subheader("📊 Function Statistics")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Min", f"{np.min(y):.4f}")
            c2.metric("Max", f"{np.max(y):.4f}")
            c3.metric("Mean", f"{np.mean(y):.4f}")
            c4.metric("Std Dev", f"{np.std(y):.4f}")

        except Exception as e:
            st.error(f"Plotting Error: {e}")

# ============================================
# 3. EQUATION SOLVER
# ============================================
elif tool == "➗ Equation Solver":
    st.header("➗ Equation & System Solver")

    solver_type = st.selectbox("Solver Type", ["Single Equation", "System of Equations", "Polynomial Roots", "Differential Equation"])

    if solver_type == "Single Equation":
        st.subheader("Solve f(x) = 0")
        eq = st.text_input("Equation (use x):", value="x**2 - 4")

        col1, col2 = st.columns(2)
        with col1:
            x_sym = sp.Symbol('x')
            try:
                expr = sp.sympify(eq)
                solutions = sp.solve(expr, x_sym)

                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.write("**Symbolic Solutions:**")
                for sol in solutions:
                    st.latex(f"x = {sp.latex(sol)}")
                st.markdown("</div>", unsafe_allow_html=True)

                # Numerical plot
                f = sp.lambdify(x_sym, expr, 'numpy')
                x_vals = np.linspace(-10, 10, 1000)
                y_vals = f(x_vals)

                fig = go.Figure()
                fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'))
                fig.add_hline(y=0, line_dash="dash", line_color="red")
                for sol in solutions:
                    if sol.is_real:
                        fig.add_vline(x=float(sol), line_dash="dash", line_color="green")
                fig.update_layout(title=f"f(x) = {eq}", xaxis_title="x", yaxis_title="f(x)", template="plotly_white")
                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.error(f"Error: {e}")

        with col2:
            st.subheader("Step-by-Step")
            try:
                steps = sp.solve(expr, x_sym, dict=True)
                st.write("Factored form:")
                st.latex(sp.latex(sp.factor(expr)))
                st.write("Expanded form:")
                st.latex(sp.latex(sp.expand(expr)))
            except:
                st.info("Step-by-step not available for this expression")

    elif solver_type == "System of Equations":
        st.subheader("Solve System of Linear Equations")
        n_eq = st.slider("Number of equations", 2, 5, 2)

        st.write("Enter coefficients (ax + by + cz = d):")
        cols = st.columns(n_eq + 1)
        variables = [sp.Symbol(f'x{i}') for i in range(n_eq)]

        equations = []
        for i in range(n_eq):
            st.write(f"--- Equation {i+1} ---")
            cols_eq = st.columns(n_eq + 1)
            coeffs = []
            for j in range(n_eq):
                coeffs.append(cols_eq[j].number_input(f"x{j} coeff", value=1.0 if i==j else 0.0, key=f"a_{i}_{j}"))
            const = cols_eq[-1].number_input("=", value=1.0, key=f"b_{i}")
            eq = sum(c * v for c, v in zip(coeffs, variables)) - const
            equations.append(eq)

        if st.button("Solve System"):
            try:
                solution = sp.solve(equations, variables)
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                if solution:
                    if isinstance(solution, dict):
                        for var, val in solution.items():
                            st.latex(f"{sp.latex(var)} = {sp.latex(val)}")
                    else:
                        for sol in solution:
                            st.write(sol)
                else:
                    st.warning("No solution or infinite solutions")
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

    elif solver_type == "Polynomial Roots":
        st.subheader("Polynomial Root Finder")
        degree = st.slider("Degree", 1, 6, 2)
        st.write("Enter coefficients (from highest to lowest degree):")
        coeffs = []
        cols = st.columns(degree + 1)
        for i in range(degree + 1):
            default = 1 if i == 0 else (0 if i < degree else -1)
            coeffs.append(cols[i].number_input(f"x^{degree-i}", value=float(default), key=f"poly_{i}"))

        if st.button("Find Roots"):
            try:
                roots = np.roots(coeffs)
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                for i, root in enumerate(roots):
                    if np.isreal(root):
                        st.write(f"Root {i+1}: {root.real:.6f}")
                    else:
                        st.write(f"Root {i+1}: {root:.6f}")
                st.markdown("</div>", unsafe_allow_html=True)

                # Plot if degree 2
                if degree == 2:
                    x = np.linspace(-10, 10, 400)
                    y = sum(c * x**(degree-i) for i, c in enumerate(coeffs))
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))
                    fig.add_hline(y=0, line_dash="dash")
                    for root in roots:
                        if np.isreal(root):
                            fig.add_vline(x=root.real, line_dash="dash", line_color="green")
                    st.plotly_chart(fig, use_container_width=True)
            except Exception as e:
                st.error(f"Error: {e}")

    elif solver_type == "Differential Equation":
        st.subheader("Ordinary Differential Equation Solver")
        st.write("Enter ODE in form: f(x, y, y') = 0")
        ode_input = st.text_input("ODE:", value="y' + 2*y - exp(x)")

        if st.button("Solve ODE"):
            try:
                x = sp.Symbol('x')
                y = sp.Function('y')
                ode = sp.sympify(ode_input.replace("y'", "Derivative(y(x), x)").replace("y", "y(x)"))
                # This is simplified - full ODE solving requires more setup
                st.info("ODE solving requires SymPy's dsolve. Enter equation in standard form.")
            except Exception as e:
                st.error(f"Error: {e}")

# ============================================
# 4. TRIGONOMETRY LAB
# ============================================
elif tool == "📐 Trigonometry Lab":
    st.header("📐 Trigonometry Laboratory")

    tab1, tab2, tab3 = st.tabs(["Unit Circle", "Triangle Solver", "Trig Identities"])

    with tab1:
        st.subheader("Interactive Unit Circle")
        angle = st.slider("Angle (degrees)", 0, 360, 45)
        angle_rad = math.radians(angle)

        fig = go.Figure()

        # Circle
        theta = np.linspace(0, 2*np.pi, 100)
        fig.add_trace(go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines',
                                line=dict(color='lightgray', width=2), name='Unit Circle'))

        # Radius
        fig.add_trace(go.Scatter(x=[0, np.cos(angle_rad)], y=[0, np.sin(angle_rad)],
                                mode='lines+markers', line=dict(color='red', width=3),
                                name=f'Angle = {angle}°'))

        # Projections
        fig.add_trace(go.Scatter(x=[np.cos(angle_rad), np.cos(angle_rad)],
                                y=[0, np.sin(angle_rad)], mode='lines',
                                line=dict(color='blue', width=2, dash='dash'), name='Sin'))
        fig.add_trace(go.Scatter(x=[0, np.cos(angle_rad)],
                                y=[np.sin(angle_rad), np.sin(angle_rad)], mode='lines',
                                line=dict(color='green', width=2, dash='dash'), name='Cos'))

        fig.update_layout(
            xaxis=dict(range=[-1.5, 1.5], scaleanchor="y"),
            yaxis=dict(range=[-1.5, 1.5]),
            title=f"Unit Circle - {angle}°",
            template="plotly_white",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("sin", f"{math.sin(angle_rad):.4f}")
        col2.metric("cos", f"{math.cos(angle_rad):.4f}")
        col3.metric("tan", f"{math.tan(angle_rad):.4f}" if abs(math.cos(angle_rad)) > 0.001 else "undefined")
        col4.metric("Radians", f"{angle_rad:.4f}")

    with tab2:
        st.subheader("Triangle Solver")
        st.write("Enter known values (leave unknown as 0):")

        col_a, col_b, col_c = st.columns(3)
        a = col_a.number_input("Side a", value=3.0)
        b = col_b.number_input("Side b", value=4.0)
        c = col_c.number_input("Side c", value=0.0)

        col_A, col_B, col_C = st.columns(3)
        A = col_A.number_input("Angle A (°)", value=0.0)
        B = col_B.number_input("Angle B (°)", value=0.0)
        C = col_C.number_input("Angle C (°)", value=0.0)

        if st.button("Solve Triangle"):
            # Law of Cosines / Sines solver (simplified)
            known_sides = sum(1 for x in [a, b, c] if x > 0)
            known_angles = sum(1 for x in [A, B, C] if x > 0)

            if known_sides == 3:
                # SSS - compute angles
                A_calc = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
                B_calc = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
                C_calc = 180 - A_calc - B_calc
                st.success(f"Angles: A={A_calc:.2f}°, B={B_calc:.2f}°, C={C_calc:.2f}°")
            elif known_sides == 2 and known_angles == 1:
                st.info("SAS or SSA case - using Law of Cosines/Sines")
            else:
                st.warning("Need at least 3 values (including at least 1 side)")

    with tab3:
        st.subheader("Trigonometric Identities")
        identity = st.selectbox("Identity", [
            "sin²(x) + cos²(x) = 1",
            "1 + tan²(x) = sec²(x)",
            "sin(2x) = 2sin(x)cos(x)",
            "cos(2x) = cos²(x) - sin²(x)",
            "sin(A+B) = sin(A)cos(B) + cos(A)sin(B)"
        ])

        x = np.linspace(0, 2*np.pi, 1000)
        fig = go.Figure()

        if "sin² + cos²" in identity:
            y = np.sin(x)**2 + np.cos(x)**2
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='sin²(x)+cos²(x)'))
            fig.add_hline(y=1, line_dash="dash", line_color="red", annotation_text="= 1")
        elif "tan²" in identity:
            y = 1 + np.tan(x)**2
            y = np.clip(y, -10, 10)
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='1+tan²(x)'))
            fig.add_trace(go.Scatter(x=x, y=1/np.cos(x)**2, mode='lines', name='sec²(x)', line=dict(dash='dash')))

        fig.update_layout(template="plotly_white", height=400)
        st.plotly_chart(fig, use_container_width=True)

# ============================================
# 5. STATISTICS STUDIO
# ============================================
elif tool == "📉 Statistics Studio":
    st.header("📉 Statistics & Data Analysis Studio")

    data_input = st.text_area("Enter data (comma or space separated):", 
                             value="12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45")

    try:
        data = [float(x.strip()) for x in data_input.replace(',', ' ').split() if x.strip()]
        data = np.array(data)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Count", len(data))
        col2.metric("Mean", f"{np.mean(data):.3f}")
        col3.metric("Median", f"{np.median(data):.3f}")
        col4.metric("Std Dev", f"{np.std(data):.3f}")

        col5, col6, col7, col8 = st.columns(4)
        col5.metric("Min", f"{np.min(data):.3f}")
        col6.metric("Max", f"{np.max(data):.3f}")
        col7.metric("Range", f"{np.max(data) - np.min(data):.3f}")
        col8.metric("Variance", f"{np.var(data):.3f}")

        st.subheader("Visualizations")
        viz_tab1, viz_tab2, viz_tab3, viz_tab4 = st.tabs(["Histogram", "Box Plot", "Q-Q Plot", "Time Series"])

        with viz_tab1:
            bins = st.slider("Bins", 5, 50, 10)
            fig = px.histogram(x=data, nbins=bins, title="Distribution Histogram",
                             labels={'x': 'Value'}, color_discrete_sequence=['#667eea'])
            fig.add_vline(x=np.mean(data), line_dash="dash", line_color="red", annotation_text="Mean")
            fig.add_vline(x=np.median(data), line_dash="dash", line_color="green", annotation_text="Median")
            st.plotly_chart(fig, use_container_width=True)

        with viz_tab2:
            fig = go.Figure()
            fig.add_trace(go.Box(y=data, name="Data", boxpoints='all', jitter=0.3,
                               marker_color='#667eea'))
            fig.update_layout(title="Box Plot", template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

        with viz_tab3:
            from scipy import stats
            theoretical = stats.norm.ppf(np.linspace(0.01, 0.99, len(data)))
            sorted_data = np.sort(data)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=theoretical, y=sorted_data, mode='markers',
                                    marker=dict(color='#667eea', size=8)))
            # Add reference line
            z = np.polyfit(theoretical, sorted_data, 1)
            p = np.poly1d(z)
            fig.add_trace(go.Scatter(x=theoretical, y=p(theoretical), mode='lines',
                                    line=dict(color='red', dash='dash'), name='Reference'))
            fig.update_layout(title="Q-Q Plot (Normal)", xaxis_title="Theoretical Quantiles",
                            yaxis_title="Sample Quantiles", template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

        with viz_tab4:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=list(range(len(data))), y=data, mode='lines+markers',
                                    line=dict(color='#667eea', width=2),
                                    marker=dict(size=6)))
            fig.update_layout(title="Data Trend", xaxis_title="Index", yaxis_title="Value",
                            template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

        # Regression
        st.subheader("Linear Regression")
        if len(data) > 1:
            x_reg = np.arange(len(data))
            slope, intercept = np.polyfit(x_reg, data, 1)
            st.write(f"Regression Line: y = {slope:.4f}x + {intercept:.4f}")

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_reg, y=data, mode='markers', name='Data',
                                    marker=dict(color='#667eea', size=8)))
            fig.add_trace(go.Scatter(x=x_reg, y=slope*x_reg + intercept, mode='lines',
                                    name='Regression', line=dict(color='red', width=2)))
            fig.update_layout(template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

            # Correlation if user provides second dataset
            st.subheader("Correlation Analysis")
            data2_input = st.text_area("Second dataset (optional, same length):", 
                                      value="10, 14, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46")
            try:
                data2 = [float(x.strip()) for x in data2_input.replace(',', ' ').split() if x.strip()]
                data2 = np.array(data2)
                if len(data) == len(data2):
                    corr = np.corrcoef(data, data2)[0, 1]
                    st.metric("Pearson Correlation", f"{corr:.4f}")

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=data, y=data2, mode='markers',
                                            marker=dict(color='#667eea', size=10, opacity=0.7)))
                    fig.update_layout(title="Scatter Plot", xaxis_title="X", yaxis_title="Y",
                                    template="plotly_white")
                    st.plotly_chart(fig, use_container_width=True)
            except:
                pass

    except Exception as e:
        st.error(f"Data parsing error: {e}")

# ============================================
# 6. MATRIX OPERATIONS
# ============================================
elif tool == "🔢 Matrix Operations":
    st.header("🔢 Matrix Calculator")

    size = st.selectbox("Matrix Size", ["2x2", "3x3", "4x4"])
    n = int(size[0])

    st.subheader("Matrix A")
    matrix_a = []
    for i in range(n):
        cols = st.columns(n)
        row = []
        for j in range(n):
            default = 1 if i == j else 0
            row.append(cols[j].number_input(f"A[{i},{j}]", value=float(default), key=f"a_{i}_{j}"))
        matrix_a.append(row)

    A = np.array(matrix_a)

    operation = st.selectbox("Operation", [
        "Determinant", "Inverse", "Eigenvalues", "Transpose", 
        "Rank", "LU Decomposition", "Add Matrix B", "Multiply by Matrix B"
    ])

    if operation in ["Add Matrix B", "Multiply by Matrix B"]:
        st.subheader("Matrix B")
        matrix_b = []
        for i in range(n):
            cols = st.columns(n)
            row = []
            for j in range(n):
                default = 1 if i == j else 0
                row.append(cols[j].number_input(f"B[{i},{j}]", value=float(default), key=f"b_{i}_{j}"))
            matrix_b.append(row)
        B = np.array(matrix_b)

    if st.button("Compute"):
        try:
            if operation == "Determinant":
                det = np.linalg.det(A)
                st.success(f"det(A) = {det:.6f}")
            elif operation == "Inverse":
                inv = np.linalg.inv(A)
                st.write("A⁻¹ =")
                st.write(inv)
                fig = px.imshow(inv, text_auto='.3f', color_continuous_scale='RdBu')
                st.plotly_chart(fig, use_container_width=True)
            elif operation == "Eigenvalues":
                eigenvalues, eigenvectors = np.linalg.eig(A)
                st.write("Eigenvalues:")
                for i, ev in enumerate(eigenvalues):
                    st.write(f"λ{i+1} = {ev}")
                st.write("Eigenvectors:")
                st.write(eigenvectors)
            elif operation == "Transpose":
                st.write("Aᵀ =")
                st.write(A.T)
            elif operation == "Rank":
                rank = np.linalg.matrix_rank(A)
                st.success(f"Rank(A) = {rank}")
            elif operation == "LU Decomposition":
                from scipy.linalg import lu
                P, L, U = lu(A)
                st.write("P =", P)
                st.write("L =", L)
                st.write("U =", U)
            elif operation == "Add Matrix B":
                st.write("A + B =")
                st.write(A + B)
            elif operation == "Multiply by Matrix B":
                st.write("A × B =")
                st.write(A @ B)
        except Exception as e:
            st.error(f"Error: {e}")

# ============================================
# 7. UNIT CONVERTER
# ============================================
elif tool == "💱 Unit Converter":
    st.header("💱 Universal Unit Converter")

    category = st.selectbox("Category", [
        "Length", "Mass", "Temperature", "Area", "Volume", 
        "Speed", "Time", "Digital Storage", "Energy", "Pressure"
    ])

    converters = {
        "Length": {
            "m": 1, "km": 1000, "cm": 0.01, "mm": 0.001, "inch": 0.0254,
            "ft": 0.3048, "yd": 0.9144, "mile": 1609.34, "nm": 1e-9
        },
        "Mass": {
            "kg": 1, "g": 0.001, "mg": 1e-6, "ton": 1000, "lb": 0.453592,
            "oz": 0.0283495, "stone": 6.35029
        },
        "Area": {
            "m²": 1, "km²": 1e6, "cm²": 1e-4, "ha": 10000, "acre": 4046.86,
            "ft²": 0.092903, "in²": 0.00064516
        },
        "Volume": {
            "m³": 1, "L": 0.001, "mL": 1e-6, "gal": 0.00378541,
            "ft³": 0.0283168, "in³": 1.6387e-5
        },
        "Speed": {
            "m/s": 1, "km/h": 0.277778, "mph": 0.44704, "knot": 0.514444, "ft/s": 0.3048
        },
        "Time": {
            "s": 1, "min": 60, "h": 3600, "day": 86400, "week": 604800,
            "month": 2.628e6, "year": 3.154e7
        },
        "Digital Storage": {
            "B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3, "TB": 1024**4
        },
        "Energy": {
            "J": 1, "kJ": 1000, "cal": 4.184, "kcal": 4184, "Wh": 3600, "kWh": 3.6e6
        },
        "Pressure": {
            "Pa": 1, "kPa": 1000, "bar": 100000, "atm": 101325, "psi": 6894.76, "mmHg": 133.322
        }
    }

    if category == "Temperature":
        col1, col2, col3 = st.columns(3)
        val = col1.number_input("Value", value=25.0)
        from_unit = col2.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = col3.selectbox("To", ["Fahrenheit", "Celsius", "Kelvin"])

        if st.button("Convert"):
            if from_unit == "Celsius":
                c = val
            elif from_unit == "Fahrenheit":
                c = (val - 32) * 5/9
            else:
                c = val - 273.15

            if to_unit == "Celsius":
                result = c
            elif to_unit == "Fahrenheit":
                result = c * 9/5 + 32
            else:
                result = c + 273.15

            st.success(f"{val} {from_unit} = {result:.4f} {to_unit}")
    else:
        col1, col2, col3 = st.columns(3)
        val = col1.number_input("Value", value=1.0)
        units = list(converters[category].keys())
        from_unit = col2.selectbox("From", units)
        to_unit = col3.selectbox("To", units[1:] if len(units) > 1 else units)

        if st.button("Convert"):
            base = val * converters[category][from_unit]
            result = base / converters[category][to_unit]
            st.success(f"{val} {from_unit} = {result:.6f} {to_unit}")

# ============================================
# 8. PROBABILITY & COMBINATORICS
# ============================================
elif tool == "🎲 Probability & Combinatorics":
    st.header("🎲 Probability & Combinatorics")

    calc_type = st.selectbox("Calculation", [
        "Factorial", "Permutations", "Combinations", "Binomial Probability",
        "Normal Distribution", "Poisson Distribution", "Random Number Generator"
    ])

    if calc_type == "Factorial":
        n = st.number_input("n", value=5, min_value=0, max_value=170, step=1)
        if st.button("Calculate"):
            st.success(f"{n}! = {math.factorial(n)}")

    elif calc_type == "Permutations":
        n = st.number_input("n", value=5, step=1)
        r = st.number_input("r", value=3, step=1)
        if st.button("Calculate"):
            result = math.factorial(n) // math.factorial(n - r)
            st.success(f"P({n},{r}) = {result}")

    elif calc_type == "Combinations":
        n = st.number_input("n", value=5, step=1)
        r = st.number_input("r", value=3, step=1)
        if st.button("Calculate"):
            result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
            st.success(f"C({n},{r}) = {result}")

    elif calc_type == "Binomial Probability":
        n = st.number_input("Trials (n)", value=10, step=1)
        p = st.slider("Probability (p)", 0.0, 1.0, 0.5)
        k = st.number_input("Successes (k)", value=5, step=1)
        if st.button("Calculate"):
            from scipy.stats import binom
            prob = binom.pmf(k, n, p)
            cum_prob = binom.cdf(k, n, p)
            st.success(f"P(X={k}) = {prob:.6f}")
            st.info(f"P(X≤{k}) = {cum_prob:.6f}")

            # Plot distribution
            x_vals = range(n + 1)
            probs = [binom.pmf(x, n, p) for x in x_vals]
            fig = go.Figure()
            fig.add_trace(go.Bar(x=list(x_vals), y=probs, marker_color='#667eea'))
            fig.add_vline(x=k, line_dash="dash", line_color="red")
            fig.update_layout(title=f"Binomial Distribution (n={n}, p={p})",
                            xaxis_title="k", yaxis_title="P(X=k)", template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

    elif calc_type == "Normal Distribution":
        mu = st.number_input("Mean (μ)", value=0.0)
        sigma = st.number_input("Std Dev (σ)", value=1.0, min_value=0.01)
        x_query = st.number_input("Find P(X ≤ x) for x =", value=1.0)

        if st.button("Calculate"):
            from scipy.stats import norm
            prob = norm.cdf(x_query, mu, sigma)
            st.success(f"P(X ≤ {x_query}) = {prob:.6f}")

            x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
            y = norm.pdf(x, mu, sigma)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', fill='tozeroy',
                                    line=dict(color='#667eea')))

            # Shade area up to x_query
            x_shade = x[x <= x_query]
            y_shade = y[x <= x_query]
            fig.add_trace(go.Scatter(x=x_shade, y=y_shade, fill='tozeroy',
                                    fillcolor='rgba(102, 126, 234, 0.3)',
                                    line=dict(color='#667eea'), name=f'P(X≤{x_query})'))

            fig.add_vline(x=x_query, line_dash="dash", line_color="red")
            fig.update_layout(title=f"Normal Distribution N({mu}, {sigma}²)",
                            template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

    elif calc_type == "Poisson Distribution":
        lam = st.number_input("Lambda (λ)", value=3.0, min_value=0.1)
        k = st.number_input("k", value=2, step=1)
        if st.button("Calculate"):
            from scipy.stats import poisson
            prob = poisson.pmf(k, lam)
            st.success(f"P(X={k}) = {prob:.6f}")

    elif calc_type == "Random Number Generator":
        st.subheader("Random Number Generator")
        count = st.slider("Count", 1, 1000, 100)
        min_val = st.number_input("Min", value=0)
        max_val = st.number_input("Max", value=100)

        if st.button("Generate"):
            numbers = np.random.uniform(min_val, max_val, count)
            st.write(numbers[:20])
            if count > 20:
                st.write(f"... and {count - 20} more")

            fig = px.histogram(x=numbers, nbins=30, title="Distribution of Random Numbers",
                             color_discrete_sequence=['#667eea'])
            st.plotly_chart(fig, use_container_width=True)

# ============================================
# 9. GEOMETRY TOOLS
# ============================================
elif tool == "📏 Geometry Tools":
    st.header("📏 Geometry Calculator")

    shape = st.selectbox("Shape", [
        "Circle", "Rectangle", "Triangle", "Sphere", "Cube", "Cylinder", "Cone"
    ])

    if shape == "Circle":
        r = st.number_input("Radius", value=5.0, min_value=0.0)
        if st.button("Calculate"):
            area = math.pi * r**2
            circ = 2 * math.pi * r
            diam = 2 * r
            col1, col2, col3 = st.columns(3)
            col1.metric("Area", f"{area:.4f}")
            col2.metric("Circumference", f"{circ:.4f}")
            col3.metric("Diameter", f"{diam:.4f}")

            theta = np.linspace(0, 2*np.pi, 100)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=r*np.cos(theta), y=r*np.sin(theta), mode='lines',
                                    fill='toself', fillcolor='rgba(102, 126, 234, 0.3)',
                                    line=dict(color='#667eea', width=2)))
            fig.update_layout(xaxis=dict(scaleanchor="y"), template="plotly_white", title="Circle")
            st.plotly_chart(fig, use_container_width=True)

    elif shape == "Rectangle":
        col1, col2 = st.columns(2)
        w = col1.number_input("Width", value=4.0, min_value=0.0)
        h = col2.number_input("Height", value=6.0, min_value=0.0)
        if st.button("Calculate"):
            area = w * h
            perim = 2 * (w + h)
            diag = math.sqrt(w**2 + h**2)
            col1, col2, col3 = st.columns(3)
            col1.metric("Area", f"{area:.4f}")
            col2.metric("Perimeter", f"{perim:.4f}")
            col3.metric("Diagonal", f"{diag:.4f}")

    elif shape == "Triangle":
        st.write("Enter three sides (SSS):")
        col1, col2, col3 = st.columns(3)
        a = col1.number_input("Side a", value=3.0)
        b = col2.number_input("Side b", value=4.0)
        c = col3.number_input("Side c", value=5.0)
        if st.button("Calculate"):
            s = (a + b + c) / 2
            area = math.sqrt(s * (s-a) * (s-b) * (s-c))
            perim = a + b + c
            st.success(f"Area = {area:.4f}, Perimeter = {perim:.4f}")

    elif shape == "Sphere":
        r = st.number_input("Radius", value=5.0, min_value=0.0)
        if st.button("Calculate"):
            vol = (4/3) * math.pi * r**3
            sa = 4 * math.pi * r**2
            col1, col2 = st.columns(2)
            col1.metric("Volume", f"{vol:.4f}")
            col2.metric("Surface Area", f"{sa:.4f}")

    elif shape == "Cube":
        s = st.number_input("Side", value=5.0, min_value=0.0)
        if st.button("Calculate"):
            vol = s**3
            sa = 6 * s**2
            diag = s * math.sqrt(3)
            col1, col2, col3 = st.columns(3)
            col1.metric("Volume", f"{vol:.4f}")
            col2.metric("Surface Area", f"{sa:.4f}")
            col3.metric("Space Diagonal", f"{diag:.4f}")

    elif shape == "Cylinder":
        col1, col2 = st.columns(2)
        r = col1.number_input("Radius", value=3.0, min_value=0.0)
        h = col2.number_input("Height", value=10.0, min_value=0.0)
        if st.button("Calculate"):
            vol = math.pi * r**2 * h
            sa = 2 * math.pi * r * (r + h)
            col1, col2 = st.columns(2)
            col1.metric("Volume", f"{vol:.4f}")
            col2.metric("Surface Area", f"{sa:.4f}")

    elif shape == "Cone":
        col1, col2 = st.columns(2)
        r = col1.number_input("Radius", value=3.0, min_value=0.0)
        h = col2.number_input("Height", value=4.0, min_value=0.0)
        if st.button("Calculate"):
            vol = (1/3) * math.pi * r**2 * h
            slant = math.sqrt(r**2 + h**2)
            sa = math.pi * r * (r + slant)
            col1, col2, col3 = st.columns(3)
            col1.metric("Volume", f"{vol:.4f}")
            col2.metric("Slant Height", f"{slant:.4f}")
            col3.metric("Surface Area", f"{sa:.4f}")

# ============================================
# 10. NUMBER THEORY
# ============================================
elif tool == "🔍 Number Theory":
    st.header("🔍 Number Theory Explorer")

    n = st.number_input("Enter a number", value=100, step=1, min_value=1)
    n = int(n)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Properties")
        is_prime = all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)) and n > 1
        st.write(f"**Prime:** {'Yes ✅' if is_prime else 'No ❌'}")

        # Factors
        factors = [i for i in range(1, n + 1) if n % i == 0]
        st.write(f"**Factors:** {factors}")

        # Prime factorization
        temp = n
        prime_factors = []
        d = 2
        while d * d <= temp:
            while temp % d == 0:
                prime_factors.append(d)
                temp //= d
            d += 1
        if temp > 1:
            prime_factors.append(temp)
        st.write(f"**Prime Factorization:** {' × '.join(map(str, prime_factors))}")

    with col2:
        st.subheader("Number Sequences")
        st.write(f"**Fibonacci up to {n}:**")
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        st.write(fib[:-1])

        st.write(f"**First {min(n, 20)} multiples:**")
        st.write([n * i for i in range(1, min(n, 20) + 1)])

    with col3:
        st.subheader("Base Conversions")
        st.write(f"**Binary:** {bin(n)[2:]}")
        st.write(f"**Octal:** {oct(n)[2:]}")
        st.write(f"**Hex:** {hex(n)[2:].upper()}")
        st.write(f"**Roman:** ", end="")

        # Roman numeral conversion
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ''
        i = 0
        temp_n = n
        while temp_n > 0:
            for _ in range(temp_n // val[i]):
                roman_num += syb[i]
                temp_n -= val[i]
            i += 1
        st.write(roman_num)

    # Sieve visualization
    st.subheader("Prime Sieve Visualization")
    limit = st.slider("Limit", 10, 200, 50)
    if st.button("Show Sieve"):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.sqrt(limit)) + 1):
            if sieve[i]:
                for j in range(i*i, limit + 1, i):
                    sieve[j] = False

        primes = [i for i, is_p in enumerate(sieve) if is_p]

        fig = go.Figure()
        colors = ['#667eea' if sieve[i] else '#e0e0e0' for i in range(limit + 1)]
        fig.add_trace(go.Bar(x=list(range(limit + 1)), 
                            y=[1] * (limit + 1),
                            marker_color=colors,
                            text=[str(i) for i in range(limit + 1)],
                            textposition='auto'))
        fig.update_layout(title=f"Prime Numbers up to {limit} (Purple = Prime)",
                         xaxis_title="Number", yaxis_visible=False,
                         template="plotly_white", height=300)
        st.plotly_chart(fig, use_container_width=True)
        st.write(f"Primes found: {len(primes)} — {primes}")

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #888; margin-top: 3rem;">
    <hr>
    <p>🔬 Math Lab | مختبر الرياضيات — Built with Streamlit & Python</p>
    <p>Made with ❤️ for mathematics enthusiasts</p>
</div>
""", unsafe_allow_html=True)
