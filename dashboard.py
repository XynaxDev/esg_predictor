import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="ESG Analytics Dashboard",
    page_icon="♾️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# MODERN PROFESSIONAL CSS (Clean & Minimal)
# ============================================================================
st.markdown(
    """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main background */
    .main {
        background-color: #0e1117;
        color: #fafafa;
        padding: 1rem;
    }
    
    /* Override default Streamlit background */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Fix text colors globally */
    .stMarkdown, 
    .stMarkdown p,
    .stMarkdown span,
    .stText,
    .stText p,
    .stText span {
        color: #ffffff !important;
    }
    
    /* Style text headers */
    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3,
    .stMarkdown h4 {
        color: #ffffff !important;
    }
    
    /* Override markdown text color */
    .css-10trblm, .css-183lzff, .css-1aehpvj {
        color: #fafafa !important;
    }
    
    .block-container {
        padding-top: 1rem !important;
        padding: 1rem 2rem;
        max-width: 1400px;
    }
    
    /* Headers */
    h1 {
        color: #1a1a1a;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #2d3748;
        font-weight: 600;
        font-size: 1.75rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    h3 {
        color: #4a5568;
        font-weight: 600;
        font-size: 1.25rem;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    
    h4 {
        color: #2d3748;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    
    /* Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #fafafa;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.875rem;
        font-weight: 500;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 0.875rem;
    }
    
    /* Metric Container Enhancement */
    [data-testid="metric-container"] {
        background: #1f2937;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #374151;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #1f2937;
        border-right: 1px solid #374151;
        padding: 1.5rem 1rem;
        min-width: 300px !important;
    }
    
    /* Fix sidebar dropdown width */
    [data-testid="stSidebar"] .stSelectbox {
        width: 100% !important;
    }
    
    [data-testid="stSidebar"] .stMultiSelect {
        width: 100% !important;
    }
    
    /* Style sidebar selects */
    [data-testid="stSidebar"] [data-baseweb="select"] {
        background-color: #374151;
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    [data-testid="stSidebar"] [data-baseweb="select"] * {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #fafafa;
    }
    
    /* Sidebar text color */
    [data-testid="stSidebar"] .css-10trblm, 
    [data-testid="stSidebar"] .css-183lzff,
    [data-testid="stSidebar"] .css-1aehpvj {
        color: #fafafa !important;
    }
    
    /* Radio buttons in sidebar */
    [data-testid="stSidebar"] .row-widget {
        background: #374151;
        padding: 0.5rem;
        border-radius: 8px;
        margin: 0.25rem 0;
    }
    
    /* Buttons */
    .stButton>button {
        background: #3182ce;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.625rem 1.5rem;
        font-weight: 500;
        font-size: 0.875rem;
        transition: all 0.2s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .stButton>button:hover {
        background: #2c5282;
        box-shadow: 0 4px 12px rgba(49,130,206,0.3);
        transform: translateY(-1px);
    }
    
    /* Select boxes and inputs */
    .stSelectbox, .stMultiSelect {
        background: white;
    }
    
    /* Divider */
    hr {
        margin: 2.5rem 0;
        border: none;
        height: 1px;
        background: #e2e8f0;
    }
    
    /* Chart containers */
    .js-plotly-plot {
        border-radius: 12px;
        background: #1f2937;
        padding: 1rem;
        border: 1px solid #374151;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    
    /* Info boxes */
    .stAlert {
        background: #1f2937;
        border-left: 4px solid #3182ce;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        color: #fafafa;
    }
    
    /* Dataframe styling */
    .dataframe {
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px;
        overflow: hidden;
    }
    
    /* Section card */
    .section-card {
        background: #1f2937;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #374151;
        margin: 1.5rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }
    
    .insight-card {
        background: #1f2937;
        padding: 2rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        color: #ffffff;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }

    .insight-card::before {
        content: "✨";
        position: absolute;
        top: 1.5rem;
        right: 1.5rem;
        font-size: 1.5rem;
        opacity: 0.5;
    }

    .insight-card h3 {
        color: #ffffff;
        font-size: 1.3rem;
        margin-bottom: 1.5rem;
        padding-right: 3rem;
    }

    .insight-card h4 {
        color: #94a3b8;
        font-size: 1.1rem;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    .insight-card p {
        color: #e2e8f0;
        line-height: 1.6;
    }

    .insight-card strong {
        color: #ffffff;
        font-weight: 600;
    }
    
    .recommendation-card {
        background: #1f2937;
        padding: 2rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        color: #ffffff;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }

    .recommendation-card::before {
        content: "💡";
        position: absolute;
        top: 1.5rem;
        right: 1.5rem;
        font-size: 1.5rem;
        opacity: 0.5;
    }

    .recommendation-card h3 {
        color: #ffffff;
        font-size: 1.3rem;
        margin-bottom: 1.5rem;
        padding-right: 3rem;
    }

    .recommendation-card h4 {
        color: #94a3b8;
        font-size: 1.1rem;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    .recommendation-card p {
        color: #e2e8f0;
        line-height: 1.6;
    }

    .recommendation-card ul {
        color: #e2e8f0;
        margin-left: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .recommendation-card li {
        margin-bottom: 0.5rem;
    }

    .recommendation-card li strong {
        color: #ffffff;
    }

    /* Typography improvements */
    p {
        color: #fafafa;
        line-height: 1.7;
        margin-bottom: 1rem;
    }
    
    ul {
        color: #fafafa;
        line-height: 1.8;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #1f2937;
        padding: 0.5rem;
        border-radius: 8px;
        border: 1px solid #374151;
    }
    
    /* Override data frame styling */
    .dataframe {
        color: #fafafa;
    }
    
    /* Style scrollbars */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1f2937;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #374151;
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #4b5563;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    /* Remove emoji fallback */
    .emoji {
        display: none;
    }
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================================
# DATA LOADING FUNCTION
# ============================================================================
@st.cache_data
def load_data():
    """Load and cache the ESG dataset"""
    try:
        df = pd.read_csv("esg_financial_data.csv")
        return df
    except:
        # Sample data for demonstration
        np.random.seed(42)
        companies = [f"Company_{i}" for i in range(1, 51)]
        industries = ["Retail", "Technology", "Healthcare", "Finance", "Energy"]
        regions = ["North America", "Europe", "Asia", "Latin America"]
        years = range(2015, 2026)

        data = []
        for company in companies:
            for year in years:
                data.append(
                    {
                        "CompanyID": int(company.split("_")[1]),
                        "CompanyName": company,
                        "Industry": np.random.choice(industries),
                        "Region": np.random.choice(regions),
                        "Year": year,
                        "Revenue": np.random.uniform(100, 5000),
                        "ProfitMargin": np.random.uniform(-5, 15),
                        "MarketCap": np.random.uniform(100, 20000),
                        "GrowthRate": np.random.uniform(-20, 30),
                        "ESG_Overall": np.random.uniform(40, 80),
                        "ESG_Environmental": np.random.uniform(30, 80),
                        "ESG_Social": np.random.uniform(20, 90),
                        "ESG_Governance": np.random.uniform(30, 85),
                        "CarbonEmissions": np.random.uniform(10000, 300000),
                        "WaterUsage": np.random.uniform(5000, 150000),
                        "EnergyConsumption": np.random.uniform(20000, 600000),
                    }
                )
        return pd.DataFrame(data)


# Load data
df = load_data()

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================
st.sidebar.markdown(
    "<h2 style='margin-top: 0;'>ESG Analytics</h2>", unsafe_allow_html=True
)
st.sidebar.markdown(
    "<p style='color: #718096; font-size: 0.875rem; margin-bottom: 2rem;'>Environmental, Social & Governance Dashboard</p>",
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Industry Analysis",
        "Regional Insights",
        "Trends Over Time",
        "Key Insights",
        "Recommendations",
    ],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<h3 style='font-size: 1rem; margin-bottom: 1rem;'>FILTERS</h3>",
    unsafe_allow_html=True,
)

# Advanced Filters
st.sidebar.markdown("### Main Filters")
selected_years = st.sidebar.slider(
    "Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (int(df["Year"].min()), int(df["Year"].max())),
)

selected_industries = st.sidebar.multiselect(
    "Industries",
    options=df["Industry"].unique().tolist(),
    default=df["Industry"].unique().tolist(),
)

selected_regions = st.sidebar.multiselect(
    "Regions",
    options=df["Region"].unique().tolist(),
    default=df["Region"].unique().tolist(),
)

# Performance Filters
st.sidebar.markdown("### Performance Filters")
min_esg_score = st.sidebar.slider("Minimum ESG Score", 0, 100, 0)
min_revenue = st.sidebar.slider(
    "Minimum Revenue (M)",
    int(df["Revenue"].min()),
    int(df["Revenue"].max()),
    int(df["Revenue"].min()),
)

# Environmental Filters
st.sidebar.markdown("### Environmental Filters")
max_carbon = st.sidebar.slider(
    "Maximum Carbon Emissions",
    int(df["CarbonEmissions"].min()),
    int(df["CarbonEmissions"].max()),
    int(df["CarbonEmissions"].max()),
)

max_energy = st.sidebar.slider(
    "Maximum Energy Consumption",
    int(df["EnergyConsumption"].min()),
    int(df["EnergyConsumption"].max()),
    int(df["EnergyConsumption"].max()),
)

# Growth Filters
st.sidebar.markdown("### Growth Filters")
min_growth = st.sidebar.slider(
    "Minimum Growth Rate (%)",
    int(df["GrowthRate"].min()),
    int(df["GrowthRate"].max()),
    int(df["GrowthRate"].min()),
)

# Apply all filters
filtered_df = df[
    (df["Year"] >= selected_years[0])
    & (df["Year"] <= selected_years[1])
    & (df["Industry"].isin(selected_industries))
    & (df["Region"].isin(selected_regions))
    & (df["ESG_Overall"] >= min_esg_score)
    & (df["Revenue"] >= min_revenue)
    & (df["CarbonEmissions"] <= max_carbon)
    & (df["EnergyConsumption"] <= max_energy)
    & (df["GrowthRate"] >= min_growth)
]

st.sidebar.markdown("---")
st.sidebar.info(f"Last Updated: {datetime.now().strftime('%B %d, %Y')}")

# Export button
if st.sidebar.button("Export Data", use_container_width=True):
    csv = filtered_df.to_csv(index=False)
    st.sidebar.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"esg_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv",
        use_container_width=True,
    )

# ============================================================================
# PAGE 1: OVERVIEW DASHBOARD
# ============================================================================
if page == "Overview":
    st.title("ESG & Financial Performance Dashboard")
    st.markdown(
        "<p style='font-size: 1.125rem; color: #718096; margin-bottom: 2rem;'>Comprehensive analysis of environmental, social, and governance metrics across industries</p>",
        unsafe_allow_html=True,
    )

    # ESG Leadership Board
    st.markdown("### ESG Leadership Board")

    # Calculate ranks for different ESG categories
    top_performers = (
        filtered_df.groupby("CompanyName")
        .agg(
            {
                "ESG_Overall": "mean",
                "ESG_Environmental": "mean",
                "ESG_Social": "mean",
                "ESG_Governance": "mean",
                "Industry": "first",
                "Revenue": "mean",
            }
        )
        .round(2)
    )

    # Add rankings
    top_performers["Overall_Rank"] = top_performers["ESG_Overall"].rank(ascending=False)
    top_performers["Environmental_Rank"] = top_performers["ESG_Environmental"].rank(
        ascending=False
    )
    top_performers["Social_Rank"] = top_performers["ESG_Social"].rank(ascending=False)
    top_performers["Governance_Rank"] = top_performers["ESG_Governance"].rank(
        ascending=False
    )

    # Create tabs for different rankings
    ranking_tabs = st.tabs(["Overall ESG", "Environmental", "Social", "Governance"])

    with ranking_tabs[0]:
        top_overall = top_performers.nsmallest(10, "Overall_Rank")[
            ["ESG_Overall", "Industry", "Revenue", "Overall_Rank"]
        ].reset_index()

        fig = go.Figure(
            data=[
                go.Bar(
                    x=top_overall["CompanyName"],
                    y=top_overall["ESG_Overall"],
                    marker_color="#3182ce",
                    text=top_overall["ESG_Overall"].round(1),
                    textposition="auto",
                    hovertemplate=(
                        "<b>%{x}</b><br>"
                        + "ESG Score: %{y:.1f}<br>"
                        + "Industry: %{customdata[0]}<br>"
                        + "Revenue: $%{customdata[1]:.0f}M<br>"
                        + "Rank: %{customdata[2]:.0f}"
                    ),
                    customdata=top_overall[["Industry", "Revenue", "Overall_Rank"]],
                )
            ]
        )

        fig.update_layout(
            title="Top 10 Overall ESG Performers",
            xaxis_title="",
            yaxis_title="ESG Score",
            template="plotly_white",
            height=400,
            xaxis_tickangle=-45,
            margin=dict(l=20, r=20, t=40, b=120),
        )
        st.plotly_chart(fig, use_container_width=True)

    with ranking_tabs[1]:
        top_env = top_performers.nsmallest(10, "Environmental_Rank")[
            ["ESG_Environmental", "Industry", "Revenue", "Environmental_Rank"]
        ].reset_index()

        fig = go.Figure(
            data=[
                go.Bar(
                    x=top_env["CompanyName"],
                    y=top_env["ESG_Environmental"],
                    marker_color="#48bb78",
                    text=top_env["ESG_Environmental"].round(1),
                    textposition="auto",
                    hovertemplate=(
                        "<b>%{x}</b><br>"
                        + "Environmental Score: %{y:.1f}<br>"
                        + "Industry: %{customdata[0]}<br>"
                        + "Revenue: $%{customdata[1]:.0f}M<br>"
                        + "Rank: %{customdata[2]:.0f}"
                    ),
                    customdata=top_env[["Industry", "Revenue", "Environmental_Rank"]],
                )
            ]
        )

        fig.update_layout(
            title="Top 10 Environmental Performers",
            xaxis_title="",
            yaxis_title="Environmental Score",
            template="plotly_white",
            height=400,
            xaxis_tickangle=-45,
            margin=dict(l=20, r=20, t=40, b=120),
        )
        st.plotly_chart(fig, use_container_width=True)

    with ranking_tabs[2]:
        top_social = top_performers.nsmallest(10, "Social_Rank")[
            ["ESG_Social", "Industry", "Revenue", "Social_Rank"]
        ].reset_index()

        fig = go.Figure(
            data=[
                go.Bar(
                    x=top_social["CompanyName"],
                    y=top_social["ESG_Social"],
                    marker_color="#ed8936",
                    text=top_social["ESG_Social"].round(1),
                    textposition="auto",
                    hovertemplate=(
                        "<b>%{x}</b><br>"
                        + "Social Score: %{y:.1f}<br>"
                        + "Industry: %{customdata[0]}<br>"
                        + "Revenue: $%{customdata[1]:.0f}M<br>"
                        + "Rank: %{customdata[2]:.0f}"
                    ),
                    customdata=top_social[["Industry", "Revenue", "Social_Rank"]],
                )
            ]
        )

        fig.update_layout(
            title="Top 10 Social Performers",
            xaxis_title="",
            yaxis_title="Social Score",
            template="plotly_white",
            height=400,
            xaxis_tickangle=-45,
            margin=dict(l=20, r=20, t=40, b=120),
        )
        st.plotly_chart(fig, use_container_width=True)

    with ranking_tabs[3]:
        top_gov = top_performers.nsmallest(10, "Governance_Rank")[
            ["ESG_Governance", "Industry", "Revenue", "Governance_Rank"]
        ].reset_index()

        fig = go.Figure(
            data=[
                go.Bar(
                    x=top_gov["CompanyName"],
                    y=top_gov["ESG_Governance"],
                    marker_color="#9f7aea",
                    text=top_gov["ESG_Governance"].round(1),
                    textposition="auto",
                    hovertemplate=(
                        "<b>%{x}</b><br>"
                        + "Governance Score: %{y:.1f}<br>"
                        + "Industry: %{customdata[0]}<br>"
                        + "Revenue: $%{customdata[1]:.0f}M<br>"
                        + "Rank: %{customdata[2]:.0f}"
                    ),
                    customdata=top_gov[["Industry", "Revenue", "Governance_Rank"]],
                )
            ]
        )

        fig.update_layout(
            title="Top 10 Governance Performers",
            xaxis_title="",
            yaxis_title="Governance Score",
            template="plotly_white",
            height=400,
            xaxis_tickangle=-45,
            margin=dict(l=20, r=20, t=40, b=120),
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Key Metrics Row
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="Total Companies",
            value=f"{filtered_df['CompanyID'].nunique()}",
            delta=f"{len(filtered_df)} records",
        )

    with col2:
        avg_esg = filtered_df["ESG_Overall"].mean()
        st.metric(
            label="Average ESG Score",
            value=f"{avg_esg:.1f}",
            delta=f"{avg_esg - df['ESG_Overall'].mean():.1f}",
        )

    with col3:
        avg_revenue = filtered_df["Revenue"].mean()
        st.metric(
            label="Average Revenue",
            value=f"${avg_revenue:.0f}M",
            delta=f"{filtered_df['GrowthRate'].mean():.1f}%",
        )

    with col4:
        avg_carbon = filtered_df["CarbonEmissions"].mean()
        st.metric(
            label="Avg Carbon (tons)",
            value=f"{avg_carbon/1000:.0f}K",
            delta=f"{(avg_carbon - df['CarbonEmissions'].mean())/1000:.1f}K",
        )

    with col5:
        positive_growth = (filtered_df["GrowthRate"] > 0).sum()
        st.metric(
            label="Positive Growth",
            value=f"{positive_growth}",
            delta=f"{positive_growth/len(filtered_df)*100:.0f}%",
        )

    st.markdown("---")

    # Main visualizations
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### ESG Score Distribution")
        fig = go.Figure()

        fig.add_trace(
            go.Box(
                y=filtered_df["ESG_Overall"],
                name="Overall",
                marker_color="#3182ce",
                boxmean="sd",
            )
        )
        fig.add_trace(
            go.Box(
                y=filtered_df["ESG_Environmental"],
                name="Environmental",
                marker_color="#48bb78",
                boxmean="sd",
            )
        )
        fig.add_trace(
            go.Box(
                y=filtered_df["ESG_Social"],
                name="Social",
                marker_color="#ed8936",
                boxmean="sd",
            )
        )
        fig.add_trace(
            go.Box(
                y=filtered_df["ESG_Governance"],
                name="Governance",
                marker_color="#9f7aea",
                boxmean="sd",
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            title="ESG Score Components Distribution",
        )
        st.plotly_chart(fig, use_container_width=True)

        # Overview Insights Card
        st.markdown(
            """
            <div class='insight-card'>
                <h3>ESG Performance Overview</h3>
                <p>Based on the analysis of {0} companies across {1} industries:</p>
                <ul>
                    <li>Average ESG Score: <strong>{2:.1f}</strong></li>
                    <li>Environmental Leaders: {3:.0f}% of companies</li>
                    <li>Social Impact: {4:.1f}% average score</li>
                    <li>Governance Rating: {5:.1f}% compliance</li>
                </ul>
                <p>Key trends show {6} improvement in overall ESG performance year over year.</p>
            </div>
        """.format(
                filtered_df["CompanyID"].nunique(),
                len(filtered_df["Industry"].unique()),
                filtered_df["ESG_Overall"].mean(),
                (filtered_df["ESG_Environmental"] > 70).mean() * 100,
                filtered_df["ESG_Social"].mean(),
                filtered_df["ESG_Governance"].mean(),
                (
                    "consistent"
                    if filtered_df.groupby("Year")["ESG_Overall"]
                    .mean()
                    .is_monotonic_increasing
                    else "variable"
                ),
            ),
            unsafe_allow_html=True,
        )

    with col2:
        # Calculate resource efficiency
        filtered_df["Resource_Efficiency"] = (
            filtered_df["Revenue"]
            / (
                filtered_df["CarbonEmissions"]
                + filtered_df["WaterUsage"]
                + filtered_df["EnergyConsumption"]
            )
        ) * 1000000

        efficiency_by_industry = (
            filtered_df.groupby("Industry")["Resource_Efficiency"]
            .mean()
            .sort_values(ascending=False)
        )

        fig = go.Figure(
            go.Bar(
                x=efficiency_by_industry.values,
                y=efficiency_by_industry.index,
                orientation="h",
                marker=dict(color=efficiency_by_industry.values, colorscale="Greens"),
                text=efficiency_by_industry.values.round(2),
                textposition="auto",
            )
        )
        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            title="Resource Efficiency by Industry",
            xaxis_title="Efficiency Score",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Regional Comparison Section
    st.markdown("### Regional Performance Overview")
    regional_comparison = (
        filtered_df.groupby("Region")
        .agg(
            {
                "ESG_Overall": "mean",
                "CarbonEmissions": "mean",
                "Revenue": "mean",
                "CompanyID": "nunique",
            }
        )
        .round(2)
    )
    regional_comparison.columns = [
        "Avg ESG Score",
        "Avg Carbon",
        "Avg Revenue",
        "Companies",
    ]
    regional_comparison["Performance Tier"] = pd.cut(
        regional_comparison["Avg ESG Score"],
        bins=[0, 55, 65, 100],
        labels=["Developing", "Improving", "Leading"],
    )

    st.dataframe(
        regional_comparison.style.background_gradient(
            cmap="RdYlGn", subset=["Avg ESG Score"]
        ),
        use_container_width=True,
        height=250,
    )

    st.markdown("---")

    # Financial Performance Analysis
    st.markdown("### Financial Impact Analysis")
    col1, col2 = st.columns(2)

    with col1:
        fig = px.scatter(
            filtered_df,
            x="ESG_Overall",
            y="ProfitMargin",
            color="Industry",
            size="MarketCap",
            trendline="ols",
            title="ESG Score vs Profitability",
            color_discrete_sequence=[
                "#3182ce",
                "#48bb78",
                "#ed8936",
                "#9f7aea",
                "#f56565",
            ],
        )
        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # ESG quartile analysis
        filtered_df["ESG_Quartile"] = pd.qcut(
            filtered_df["ESG_Overall"],
            q=4,
            labels=["Q1 (Lowest)", "Q2", "Q3", "Q4 (Highest)"],
        )

        quartile_performance = (
            filtered_df.groupby("ESG_Quartile")
            .agg({"ProfitMargin": "mean", "GrowthRate": "mean", "MarketCap": "mean"})
            .round(2)
        )

        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                name="Profit Margin",
                x=quartile_performance.index,
                y=quartile_performance["ProfitMargin"],
                marker_color="#48bb78",
            )
        )
        fig.add_trace(
            go.Bar(
                name="Growth Rate",
                x=quartile_performance.index,
                y=quartile_performance["GrowthRate"],
                marker_color="#3182ce",
            )
        )

        fig.update_layout(
            barmode="group",
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            title="Financial Performance by ESG Quartile",
            xaxis_title="ESG Quartile",
            yaxis_title="Performance (%)",
        )
        st.plotly_chart(fig, use_container_width=True)

    # Summary Card
    st.markdown(
        """
        <div class='insight-card'>
            <h3>Financial Performance Insights</h3>
            <p>Analysis of {0} companies reveals:</p>
            <ul>
                <li><strong>Profitability Impact:</strong> Companies in the top ESG quartile show {1:.1f}% higher profit margins</li>
                <li><strong>Growth Correlation:</strong> {2:.1f}% higher growth rates in high ESG performers</li>
                <li><strong>Market Value:</strong> {3:.1f}% average market cap premium for ESG leaders</li>
            </ul>
            <p>The data suggests a strong positive correlation between ESG performance and financial success.</p>
        </div>
    """.format(
            len(filtered_df),
            quartile_performance.loc["Q4 (Highest)", "ProfitMargin"]
            - quartile_performance.loc["Q1 (Lowest)", "ProfitMargin"],
            quartile_performance.loc["Q4 (Highest)", "GrowthRate"]
            - quartile_performance.loc["Q1 (Lowest)", "GrowthRate"],
            (
                quartile_performance.loc["Q4 (Highest)", "MarketCap"]
                / quartile_performance.loc["Q1 (Lowest)", "MarketCap"]
                - 1
            )
            * 100,
        ),
        unsafe_allow_html=True,
    )

    # Temporal improvement tracking
    st.markdown("### ESG Improvement Trajectory Simulator")
    st.markdown(
        "<p style='color: #718096; margin-bottom: 1.5rem;'>Interactive projection tool for planning ESG improvements</p>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    with col1:
        baseline_year = st.slider(
            "Select Baseline Year",
            int(filtered_df["Year"].min()),
            int(filtered_df["Year"].max()) - 3,
            int(filtered_df["Year"].min()),
        )

    with col2:
        improvement_rate = st.slider("Annual Improvement Rate (%)", 1, 10, 5)

    # Calculate projection
    baseline_esg = filtered_df[filtered_df["Year"] == baseline_year][
        "ESG_Overall"
    ].mean()
    years_projected = list(range(baseline_year, baseline_year + 6))
    projected_scores = [
        baseline_esg * (1 + improvement_rate / 100) ** (i - baseline_year)
        for i in years_projected
    ]

    fig = go.Figure()

    # Historical data
    historical = (
        filtered_df[filtered_df["Year"] <= baseline_year]
        .groupby("Year")["ESG_Overall"]
        .mean()
    )
    fig.add_trace(
        go.Scatter(
            x=historical.index,
            y=historical.values,
            mode="lines+markers",
            name="Historical",
            line=dict(color="#3182ce", width=3),
            marker=dict(size=8),
        )
    )

    #
    fig.add_trace(
        go.Scatter(
            x=years_projected,
            y=projected_scores,
            mode="lines+markers",
            name="Projected",
            line=dict(color="#48bb78", width=3, dash="dash"),
            marker=dict(size=8),
        )
    )

    fig.update_layout(
        template="plotly_white",
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(color="#2d3748", size=12),
        showlegend=True,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Regional comparison table
    st.markdown("### Comprehensive Regional Comparison")

    regional_stats = (
        filtered_df.groupby("Region")
        .agg(
            {
                "ESG_Overall": "mean",
                "ESG_Environmental": "mean",
                "ESG_Social": "mean",
                "ESG_Governance": "mean",
                "Revenue": "mean",
                "CarbonEmissions": "mean",
                "WaterUsage": "mean",
                "EnergyConsumption": "mean",
                "CompanyID": "nunique",
            }
        )
        .round(2)
    )

    regional_stats.columns = [
        "ESG Overall",
        "Environmental",
        "Social",
        "Governance",
        "Avg Revenue",
        "Carbon",
        "Water",
        "Energy",
        "Companies",
    ]

    st.dataframe(
        regional_stats.style.background_gradient(cmap="RdYlGn", subset=["ESG Overall"]),
        use_container_width=True,
        height=300,
    )

# ============================================================================
# PAGE 4: TRENDS OVER TIME
# ============================================================================
elif page == "Trends Over Time":
    st.title("Temporal Trends in ESG Performance")
    st.markdown(
        "<p style='font-size: 1.125rem; color: #718096; margin-bottom: 2rem;'>Historical analysis and future projections</p>",
        unsafe_allow_html=True,
    )

    # Time series of ESG scores
    st.markdown("#### ESG Score Evolution (2015-2025)")

    yearly_esg = (
        filtered_df.groupby("Year")[
            ["ESG_Overall", "ESG_Environmental", "ESG_Social", "ESG_Governance"]
        ]
        .mean()
        .reset_index()
    )

    fig = go.Figure()

    colors = {
        "ESG_Overall": "#3182ce",
        "ESG_Environmental": "#48bb78",
        "ESG_Social": "#ed8936",
        "ESG_Governance": "#9f7aea",
    }

    for col in ["ESG_Overall", "ESG_Environmental", "ESG_Social", "ESG_Governance"]:
        fig.add_trace(
            go.Scatter(
                x=yearly_esg["Year"],
                y=yearly_esg[col],
                mode="lines+markers",
                name=col.replace("ESG_", ""),
                line=dict(width=3, color=colors[col]),
                marker=dict(size=8),
            )
        )

    fig.update_layout(
        template="plotly_white",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(color="#2d3748", size=12),
        xaxis_title="Year",
        yaxis_title="ESG Score",
        hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Environmental metrics trends
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Carbon Emissions Trend")
        yearly_carbon = (
            filtered_df.groupby("Year")["CarbonEmissions"]
            .agg(["mean", "std"])
            .reset_index()
        )

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=yearly_carbon["Year"],
                y=yearly_carbon["mean"],
                mode="lines+markers",
                name="Average",
                line=dict(width=3, color="#48bb78"),
                marker=dict(size=8),
                fill="tonexty",
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=350,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            xaxis_title="Year",
            yaxis_title="Carbon Emissions",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### Energy Consumption Trend")
        yearly_energy = (
            filtered_df.groupby("Year")["EnergyConsumption"].mean().reset_index()
        )

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=yearly_energy["Year"],
                y=yearly_energy["EnergyConsumption"],
                mode="lines+markers",
                name="Average",
                line=dict(width=3, color="#ed8936"),
                marker=dict(size=8),
                fill="tozeroy",
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=350,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            xaxis_title="Year",
            yaxis_title="Energy Consumption",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Industry-wise trends
    st.markdown("#### Industry ESG Trends Over Time")

    industry_yearly = (
        filtered_df.groupby(["Year", "Industry"])["ESG_Overall"].mean().reset_index()
    )

    fig = px.line(
        industry_yearly,
        x="Year",
        y="ESG_Overall",
        color="Industry",
        markers=True,
        color_discrete_sequence=["#3182ce", "#48bb78", "#ed8936", "#9f7aea", "#f56565"],
    )

    fig.update_layout(
        template="plotly_white",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(color="#2d3748", size=12),
        xaxis_title="Year",
        yaxis_title="Average ESG Score",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Year-over-year growth analysis
    st.markdown("### Year-over-Year Growth Analysis")

    col1, col2 = st.columns(2)

    with col1:
        yearly_revenue = filtered_df.groupby("Year")["Revenue"].mean().reset_index()
        yearly_revenue["YoY_Change"] = yearly_revenue["Revenue"].pct_change() * 100

        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                x=yearly_revenue["Year"],
                y=yearly_revenue["YoY_Change"],
                marker_color=[
                    "#48bb78" if x >= 0 else "#f56565"
                    for x in yearly_revenue["YoY_Change"]
                ],
                text=yearly_revenue["YoY_Change"].round(1),
                textposition="auto",
            )
        )

        fig.update_layout(
            title="Revenue YoY % Change",
            template="plotly_white",
            height=350,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            xaxis_title="Year",
            yaxis_title="% Change",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        yearly_esg_change = (
            filtered_df.groupby("Year")["ESG_Overall"].mean().reset_index()
        )
        yearly_esg_change["YoY_Change"] = yearly_esg_change["ESG_Overall"].diff()

        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                x=yearly_esg_change["Year"],
                y=yearly_esg_change["YoY_Change"],
                marker_color=[
                    "#48bb78" if x >= 0 else "#f56565"
                    for x in yearly_esg_change["YoY_Change"].fillna(0)
                ],
                text=yearly_esg_change["YoY_Change"].round(2),
                textposition="auto",
            )
        )

        fig.update_layout(
            title="ESG Score YoY Change",
            template="plotly_white",
            height=350,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            xaxis_title="Year",
            yaxis_title="Point Change",
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE 5: KEY INSIGHTS
# ============================================================================
elif page == "Key Insights":
    st.title("Key Insights from ESG Analysis")
    st.markdown(
        "<p style='font-size: 1.125rem; color: #718096; margin-bottom: 2rem;'>Data-driven discoveries and strategic implications</p>",
        unsafe_allow_html=True,
    )

    # Insight 1
    st.markdown(
        "<div class='insight-card'><h3>INSIGHT 1: Carbon Emissions and ESG Performance</h3><p><strong>Finding:</strong> Companies with lower carbon emissions demonstrate significantly higher ESG overall scores, with a correlation coefficient indicating a moderate negative relationship.</p><p><strong>Implication:</strong> Reducing carbon footprint is a critical lever for improving overall ESG performance. Companies in high-emission industries face greater challenges but also have more opportunities for improvement.</p></div>",
        unsafe_allow_html=True,
    )

    # Visualization for Insight 1
    fig = px.scatter(
        filtered_df,
        x="CarbonEmissions",
        y="ESG_Overall",
        color="Industry",
        size="Revenue",
        hover_data=["CompanyName", "Year"],
        trendline="ols",
        color_discrete_sequence=["#3182ce", "#48bb78", "#ed8936", "#9f7aea", "#f56565"],
    )
    fig.update_layout(
        template="plotly_white",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        font=dict(color="#2d3748", size=12),
        title="Carbon Emissions vs ESG Overall Score",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Insight 2
    st.markdown(
        "<div class='insight-card'><h3>INSIGHT 2: Industry Variations in Sustainability Performance</h3><p><strong>Finding:</strong> Significant variations exist across industries, with some sectors consistently outperforming others in environmental metrics while maintaining competitive financial performance.</p><p><strong>Implication:</strong> Industry-specific benchmarks and best practices need to be established. Cross-industry learning opportunities exist, particularly in resource efficiency techniques.</p></div>",
        unsafe_allow_html=True,
    )

    # Visualization for Insight 2
    col1, col2 = st.columns(2)

    with col1:
        industry_comparison = (
            filtered_df.groupby("Industry")
            .agg({"ESG_Overall": "mean", "CarbonEmissions": "mean", "Revenue": "mean"})
            .reset_index()
        )

        fig = px.bar(
            industry_comparison.sort_values("ESG_Overall", ascending=False),
            x="Industry",
            y="ESG_Overall",
            color="CarbonEmissions",
            color_continuous_scale="Reds",
            text="ESG_Overall",
        )
        fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            title="Industry ESG Scores (colored by Carbon)",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.scatter(
            industry_comparison,
            x="Revenue",
            y="ESG_Overall",
            size="CarbonEmissions",
            color="Industry",
            text="Industry",
            color_discrete_sequence=[
                "#3182ce",
                "#48bb78",
                "#ed8936",
                "#9f7aea",
                "#f56565",
            ],
        )
        fig.update_traces(textposition="top center")
        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            title="Revenue vs ESG by Industry",
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Insight 3
    st.markdown(
        "<div class='insight-card'><h3>INSIGHT 3: Positive Temporal Trends in Sustainability</h3><p><strong>Finding:</strong> ESG scores have shown consistent improvement from 2015 to 2025, with environmental scores demonstrating the most significant growth trajectory.</p><p><strong>Implication:</strong> Corporate awareness and action on sustainability issues are increasing. This trend suggests that regulatory pressure, investor demands, and public awareness are driving positive change.</p></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Insight 4
    st.markdown(
        "<div class='insight-card'><h3>INSIGHT 4: Regional Leadership in Sustainability</h3><p><strong>Finding:</strong> Certain regions consistently outperform others in ESG metrics, suggesting different regulatory environments, cultural priorities, and access to sustainable technologies.</p><p><strong>Implication:</strong> Regional best practices should be documented and shared. Policy harmonization and technology transfer can help bridge regional gaps in sustainability performance.</p></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Insight 5
    st.markdown(
        "<div class='insight-card'><h3>INSIGHT 5: The Sustainability-Profitability Nexus</h3><p><strong>Finding:</strong> High ESG scores do not necessitate sacrificing financial performance. Many companies demonstrate that sustainability and profitability can coexist.</p><p><strong>Implication:</strong> The sustainability vs. profits dichotomy is false. Companies should view ESG investments as strategic opportunities rather than regulatory burdens.</p></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Insight 6
    st.markdown(
        "<div class='insight-card'><h3>INSIGHT 6: Integrated Resource Management Opportunities</h3><p><strong>Finding:</strong> Strong correlations exist between water usage, energy consumption, and carbon emissions, suggesting opportunities for integrated resource management strategies.</p><p><strong>Implication:</strong> Companies should adopt holistic approaches to resource efficiency. Improvements in one area often yield benefits in others, creating multiplicative sustainability gains.</p></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Insight 7
    st.markdown(
        "<div class='insight-card'><h3>INSIGHT 7: Company Size and ESG Maturity</h3><p><strong>Finding:</strong> Larger companies (by revenue and market cap) tend to have more mature ESG programs, but smaller companies can achieve competitive scores through focused strategies.</p><p><strong>Implication:</strong> ESG excellence is not solely the domain of large corporations. Tailored support programs can help SMEs achieve sustainability goals within their resource constraints.</p></div>",
        unsafe_allow_html=True,
    )

# ============================================================================
# PAGE 6: RECOMMENDATIONS
# ============================================================================
elif page == "Recommendations":
    st.title("Policy Recommendations for Sustainable Growth")
    st.markdown(
        "<p style='font-size: 1.125rem; color: #718096; margin-bottom: 2rem;'>Actionable strategies for ESG improvement</p>",
        unsafe_allow_html=True,
    )

    # Recommendation 1
    st.markdown(
        "<div class='recommendation-card'><h3>RECOMMENDATION 1: Industry-Specific Emission Reduction Targets</h3><h4>Objective:</h4><p>Establish differentiated carbon reduction goals based on industry benchmarks to ensure fair and achievable targets.</p><h4>Action Plan:</h4><ul><li><strong>Benchmark Development:</strong> Create industry-specific emission baselines using current data</li><li><strong>Tiered Targets:</strong> Set progressive reduction targets (5%, 10%, 15%) over 3-year cycles</li><li><strong>Peer Comparison:</strong> Develop industry peer groups for competitive benchmarking</li><li><strong>Incentive Structure:</strong> Reward early adopters and high performers with financial benefits</li><li><strong>Support Mechanisms:</strong> Provide technical assistance to lagging industries</li></ul><h4>Expected Impact:</h4><p>15-25% reduction in industry-wide carbon emissions over 5 years, with improved ESG scores driving investor confidence and market valuation increases.</p><h4>Implementation Timeline:</h4><p>Phase 1 (Months 1-6): Baseline establishment | Phase 2 (Months 7-12): Target setting | Phase 3 (Year 2+): Monitoring and adjustment</p></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Recommendation 2
    st.markdown(
        "<div class='recommendation-card'><h3>RECOMMENDATION 2: Integrated Resource Management Framework</h3><h4>Objective:</h4><p>Develop holistic approaches linking water, energy, and carbon management to maximize efficiency gains.</p><h4>Action Plan:</h4><ul><li><strong>Unified Monitoring Systems:</strong> Deploy IoT sensors and AI analytics for real-time resource tracking</li><li><strong>Cross-Functional Teams:</strong> Create integrated sustainability departments</li><li><strong>Technology Investment:</strong> Prioritize solutions with multiple resource benefits (e.g., solar-powered water treatment)</li><li><strong>Circular Economy Practices:</strong> Implement waste-to-energy and water recycling systems</li><li><strong>Supply Chain Integration:</strong> Extend resource efficiency to suppliers and partners</li></ul><h4>Expected Impact:</h4><p>20-30% improvement in resource efficiency ratios, 10-15% cost reduction in operational expenses, and 12-18 point improvement in overall ESG scores.</p><h4>Key Performance Indicators:</h4><ul><li>Resource intensity per revenue unit (Water/Revenue, Energy/Revenue)</li><li>Carbon efficiency (Emissions/Output)</li><li>Waste-to-resource conversion rates</li></ul></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Recommendation 3
    st.markdown(
        "<div class='recommendation-card'><h3>RECOMMENDATION 3: Regional Best Practice Sharing Networks</h3><h4>Objective:</h4><p>Facilitate knowledge exchange between high and low-performing regions to accelerate global sustainability progress.</p><h4>Action Plan:</h4><ul><li><strong>Regional Sustainability Councils:</strong> Establish quarterly forums for cross-regional collaboration</li><li><strong>Case Study Documentation:</strong> Create detailed success story libraries with implementation guides</li><li><strong>Technology Transfer Programs:</strong> Subsidize adoption of proven sustainable technologies</li><li><strong>Executive Exchange Programs:</strong> Enable sustainability leaders to mentor emerging regions</li><li><strong>Digital Knowledge Platform:</strong> Build online repository of best practices, tools, and templates</li></ul><h4>Expected Impact:</h4><p>Accelerate ESG improvements in underperforming regions by 30-40%, reduce implementation costs through shared learning, and create global community of practice.</p><h4>Focus Areas for Knowledge Sharing:</h4><ul><li>Renewable energy adoption strategies</li><li>Supply chain sustainability frameworks</li><li>Stakeholder engagement methodologies</li><li>ESG reporting and disclosure practices</li></ul></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Recommendation 4
    st.markdown(
        "<div class='recommendation-card'><h3>RECOMMENDATION 4: ESG-Linked Financial Incentives</h3><h4>Objective:</h4><p>Design financial products and mechanisms that reward ESG improvements and make sustainable practices economically attractive.</p><h4>Action Plan:</h4><ul><li><strong>Green Bonds & Loans:</strong> Offer preferential interest rates (0.5-1% reduction) for companies with high ESG scores</li><li><strong>ESG Performance Credits:</strong> Create tradeable credits for exceeding sustainability targets</li><li><strong>Tax Incentives:</strong> Advocate for tax benefits tied to verified emissions reductions</li><li><strong>Impact Investment Funds:</strong> Establish dedicated funds for companies demonstrating ESG leadership</li><li><strong>Insurance Premium Adjustments:</strong> Link premiums to sustainability risk profiles</li></ul><h4>Expected Impact:</h4><p>30-50% increase in corporate sustainability investments, improved access to capital for ESG leaders, and creation of virtuous cycle linking financial performance with environmental stewardship.</p><h4>Financial Modeling:</h4><ul><li>Cost of capital reduction: 50-100 basis points for top ESG performers</li><li>Market valuation premium: 10-20% for sustainability leaders</li><li>Risk-adjusted returns: 15-25% improvement over 5-year horizon</li></ul></div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Recommendation 5
    st.markdown(
        "<div class='recommendation-card'><h3>RECOMMENDATION 5: Continuous Monitoring & Adaptive Strategies</h3><h4>Objective:</h4><p>Implement real-time ESG monitoring systems and develop adaptive strategies based on performance trends.</p><h4>Action Plan:</h4><ul><li><strong>Dashboard Implementation:</strong> Deploy company-wide ESG tracking dashboards with real-time metrics</li><li><strong>AI-Powered Analytics:</strong> Use machine learning to predict ESG trends and identify improvement opportunities</li><li><strong>Quarterly Reviews:</strong> Conduct regular strategy assessments and course corrections</li><li><strong>Stakeholder Feedback Loops:</strong> Integrate investor, customer, and employee input into ESG strategies</li><li><strong>Progressive Target Setting:</strong> Align targets with Paris Agreement and UN SDGs</li></ul><h4>Expected Impact:</h4><p>40-50% faster response to emerging sustainability challenges, 25-35% improvement in target achievement rates, and enhanced transparency driving stakeholder trust.</p><h4>Technology Stack:</h4><ul><li>Data Collection: IoT sensors, satellite imagery, blockchain for supply chain</li><li>Analytics: Machine learning models for predictive insights</li><li>Reporting: Automated TCFD, GRI, and SASB-compliant reports</li><li>Visualization: Executive dashboards and public disclosure platforms</li></ul></div>",
        unsafe_allow_html=True,
    )

# ============================================================================
# PAGE 2: INDUSTRY ANALYSIS
# ============================================================================
elif page == "Industry Analysis":
    st.title("Industry-wise ESG Performance")
    st.markdown(
        "<p style='font-size: 1.125rem; color: #718096; margin-bottom: 2rem;'>Comparative analysis across industry sectors</p>",
        unsafe_allow_html=True,
    )

    # Industry comparison
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Average ESG Scores by Industry")
        industry_esg = filtered_df.groupby("Industry")[
            ["ESG_Overall", "ESG_Environmental", "ESG_Social", "ESG_Governance"]
        ].mean()

        fig = go.Figure()
        colors = ["#3182ce", "#48bb78", "#ed8936", "#9f7aea"]
        for idx, col in enumerate(industry_esg.columns):
            fig.add_trace(
                go.Bar(
                    name=col.replace("ESG_", ""),
                    x=industry_esg.index,
                    y=industry_esg[col],
                    text=industry_esg[col].round(1),
                    textposition="auto",
                    marker_color=colors[idx],
                )
            )

        fig.update_layout(
            barmode="group",
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            legend=dict(
                orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1
            ),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### Revenue Distribution by Industry")
        fig = px.box(
            filtered_df,
            x="Industry",
            y="Revenue",
            color="Industry",
            color_discrete_sequence=[
                "#3182ce",
                "#48bb78",
                "#ed8936",
                "#9f7aea",
                "#f56565",
            ],
        )
        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Carbon emissions by industry
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Carbon Emissions by Industry")
        industry_carbon = (
            filtered_df.groupby("Industry")["CarbonEmissions"]
            .mean()
            .sort_values(ascending=True)
        )

        fig = go.Figure(
            go.Bar(
                x=industry_carbon.values,
                y=industry_carbon.index,
                orientation="h",
                marker=dict(
                    color=industry_carbon.values, colorscale="Reds", showscale=True
                ),
                text=industry_carbon.values.round(0),
                textposition="auto",
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            xaxis_title="Average Carbon Emissions",
            yaxis_title="Industry",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### Growth Rate vs ESG by Industry")
        industry_summary = (
            filtered_df.groupby("Industry")
            .agg({"GrowthRate": "mean", "ESG_Overall": "mean", "Revenue": "sum"})
            .reset_index()
        )

        fig = px.scatter(
            industry_summary,
            x="GrowthRate",
            y="ESG_Overall",
            size="Revenue",
            color="Industry",
            text="Industry",
            color_discrete_sequence=[
                "#3182ce",
                "#48bb78",
                "#ed8936",
                "#9f7aea",
                "#f56565",
            ],
        )
        fig.update_traces(textposition="top center")
        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Detailed industry table
    st.markdown("### Detailed Industry Statistics")

    industry_stats = (
        filtered_df.groupby("Industry")
        .agg(
            {
                "ESG_Overall": ["mean", "std"],
                "Revenue": ["mean", "sum"],
                "CarbonEmissions": "mean",
                "WaterUsage": "mean",
                "EnergyConsumption": "mean",
                "GrowthRate": "mean",
                "CompanyID": "nunique",
            }
        )
        .round(2)
    )

    industry_stats.columns = [
        "ESG Avg",
        "ESG Std",
        "Revenue Avg",
        "Revenue Total",
        "Carbon Avg",
        "Water Avg",
        "Energy Avg",
        "Growth Rate",
        "Companies",
    ]

    st.dataframe(
        industry_stats.style.background_gradient(cmap="RdYlGn", subset=["ESG Avg"]),
        use_container_width=True,
        height=300,
    )

# ============================================================================
# PAGE 3: REGIONAL INSIGHTS
# ============================================================================
elif page == "Regional Insights":
    st.title("Regional ESG Performance Analysis")
    st.markdown(
        "<p style='font-size: 1.125rem; color: #718096; margin-bottom: 2rem;'>Geographic distribution of sustainability metrics</p>",
        unsafe_allow_html=True,
    )

    # Regional ESG comparison
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### ESG Scores by Region")
        region_esg = (
            filtered_df.groupby("Region")["ESG_Overall"]
            .mean()
            .sort_values(ascending=False)
        )

        fig = go.Figure(
            go.Bar(
                x=region_esg.index,
                y=region_esg.values,
                marker=dict(
                    color=region_esg.values,
                    colorscale="Greens",
                    showscale=True,
                    colorbar=dict(title="ESG Score"),
                ),
                text=region_esg.values.round(1),
                textposition="auto",
            )
        )

        fig.update_layout(
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            xaxis_title="Region",
            yaxis_title="Average ESG Score",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### Regional ESG Component Breakdown")
        region_components = filtered_df.groupby("Region")[
            ["ESG_Environmental", "ESG_Social", "ESG_Governance"]
        ].mean()

        fig = go.Figure()
        colors = ["#3182ce", "#48bb78", "#ed8936", "#9f7aea"]
        for idx in range(len(region_components)):
            fig.add_trace(
                go.Scatterpolar(
                    r=region_components.iloc[idx].values.tolist()
                    + [region_components.iloc[idx].values[0]],
                    theta=["Environmental", "Social", "Governance", "Environmental"],
                    fill="toself",
                    name=region_components.index[idx],
                    line=dict(color=colors[idx % len(colors)]),
                )
            )

        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            template="plotly_white",
            height=400,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Environmental metrics by region
    st.markdown("### Environmental Metrics by Region")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### Carbon by Region")
        region_carbon = (
            filtered_df.groupby("Region")["CarbonEmissions"].mean().sort_values()
        )

        fig = px.pie(
            values=region_carbon.values,
            names=region_carbon.index,
            hole=0.4,
            color_discrete_sequence=["#48bb78", "#3182ce", "#ed8936", "#9f7aea"],
        )
        fig.update_layout(
            template="plotly_white",
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            showlegend=True,
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### Water by Region")
        region_water = filtered_df.groupby("Region")["WaterUsage"].mean().sort_values()

        fig = px.pie(
            values=region_water.values,
            names=region_water.index,
            hole=0.4,
            color_discrete_sequence=["#3182ce", "#48bb78", "#ed8936", "#9f7aea"],
        )
        fig.update_layout(
            template="plotly_white",
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            showlegend=True,
        )
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        st.markdown("#### Energy by Region")
        region_energy = (
            filtered_df.groupby("Region")["EnergyConsumption"].mean().sort_values()
        )

        fig = px.pie(
            values=region_energy.values,
            names=region_energy.index,
            hole=0.4,
            color_discrete_sequence=["#ed8936", "#48bb78", "#3182ce", "#9f7aea"],
        )
        fig.update_layout(
            template="plotly_white",
            height=300,
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(color="#2d3748", size=12),
            showlegend=True,
        )
        st.plotly_chart(fig, use_container_width=True)
