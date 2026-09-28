#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# parameter values

E_h = 48 / 1_000_000    # Annual emissions of an ordinary household

H = 130_000_000    # Total of U.S households
Lambda = 0.1    # Portion of rich households 
m_e = 2.85    # Rich household’s emission multiplier

alpha = 5.25    # Multiplier for the excess emissions of the climate-advocate celebrity relative to the U.S. household
beta = 19.9    #  Multiplier for the excess emissions of the EV_industry innovator relative to the U.S. household
gamma = 19.9    #Multiplier for the excess emissions of the climate-skeptical politician relative to the U.S. household

theta_d = 0.82    # The domestic share of total consumption
theta_nd = 0.18    # The non-domestic share of total consumption

R_inf_CA = 0.03    # Climate advocate celebrity’s social influence


n_EV_sell = 1_300_000    # Total annual number of EV sold in the U.S. in 2024
n_EV_pro = 1_100_000    # Number of EVs produced annually in the U.S.

E_r = 3.5    # Emissions reduction from driving one EV instead of an ICE
E_ext = 3.2    # Additional emissions of producing one EV compared to an ICE

delta = 0.47    # Percentage reduction in EV productions under climate-skeptical presidency effect
sigma = 0.47    # Percentage reduction in EV sales under climate-skeptical presidency effect

m_1 = 2    # EV market expansion multiplier under climate-supportive policy 
m_2 = 1    # EV market expansion multiplier under climate-skeptical policy


S_p = 1    # Climate-skeptical presidency effect


# In[3]:


# Reference parameter values for roles and thresholds

R_v0 = 1    # Reference value of voting role in Scenarios 2,3, and 4
R_v0_CS = 1.1    # Reference value of voting role in Scenarios 5 and 6  
R_p0 = 0.7    # Reference value of politician role
R_f0 = 0.8    # Reference value of firm-manager role
p = 1    # Politician role threshold determining the EV-policy regime
v = 1    # Voter role threshold for election of climate skeptical president    


# Scenario 1:

# In[4]:


def scenario_1(E_h, H, Lambda, m_e, alpha, beta, gamma, theta_d, theta_nd):

    # Illustrative ultra-rich actors' footprints

    climate_advocate_celebrity_footprint = alpha * E_h
    EV_industry_innovator_footprint = beta * E_h
    climate_skeptical_politician_footprint = gamma * E_h

    illustrative_actors_footprint = (
        climate_advocate_celebrity_footprint
        + EV_industry_innovator_footprint
        + climate_skeptical_politician_footprint
    )


    # Ordinary and rich households' footprints

    ordinary_households_footprint = (
        (1 - Lambda) * H * E_h
    )

    rich_households_footprint = (
        (Lambda * H - 3) * m_e * E_h
        + illustrative_actors_footprint
    )


    # Consumer role

    consumer_role = (
        rich_households_footprint
        + ordinary_households_footprint
    )


    # Domestic and non-domestic consumption

    domestic_households_consumption = (
        theta_d * consumer_role
    )

    non_domestic_households_consumption = (
        theta_nd * consumer_role
    )


    # Total emissions

    emissions = (
        domestic_households_consumption
        + non_domestic_households_consumption
    )

    return emissions


# In[5]:


#Carbon footprint of the U.S. society

emissions_s1 = scenario_1(E_h, H, Lambda, m_e, alpha, beta, gamma, theta_d, theta_nd)

print(emissions_s1)


# Scenario 2:

# In[6]:


def scenario_2(
    E_h, H, Lambda, m_e,
    alpha, beta, gamma,
    theta_d, theta_nd,
    R_v0, R_p0, R_f0
):

    # Illustrative ultra-rich actors' footprints

    climate_advocate_celebrity_footprint = alpha * E_h
    EV_industry_innovator_footprint = beta * E_h
    climate_skeptical_politician_footprint = gamma * E_h

    illustrative_actors_footprint = (
        climate_advocate_celebrity_footprint
        + EV_industry_innovator_footprint
        + climate_skeptical_politician_footprint
    )


    # Ordinary and rich households' footprints

    ordinary_households_footprint = (
        (1 - Lambda) * H * E_h
    )

    rich_households_footprint = (
        (Lambda * H - 3) * m_e * E_h
        + illustrative_actors_footprint
    )


    # Consumer role

    consumer_role = (
        rich_households_footprint
        + ordinary_households_footprint
    )


    # Voter role

    voter_role = R_v0


    # Politician role

    politician_role = R_p0 * voter_role


    # Firm-manager role

    firm_manager_role = R_f0 * politician_role


    # Domestic and non-domestic consumption

    domestic_households_consumption = (
        politician_role
        * firm_manager_role
        * theta_d
        * consumer_role
    )

    non_domestic_households_consumption = (
        politician_role
        * theta_nd
        * consumer_role
    )


    # Total emissions

    emissions = (
        domestic_households_consumption
        + non_domestic_households_consumption
    )

    return emissions


# In[7]:


# Climate lifeprint of the U.S. society

emissions_s2 = scenario_2(
    E_h, H, Lambda, m_e,
    alpha, beta, gamma,
    theta_d, theta_nd,
    R_v0, R_p0, R_f0
)

print(emissions_s2)


# In[8]:


# Scenario 3

def scenario_3(
    E_h, H, Lambda, m_e,
    alpha, beta, gamma,
    theta_d, theta_nd,
    R_v0, R_p0, R_f0,
    R_inf_CA
):

    # Illustrative ultra-rich actors' footprints

    climate_advocate_celebrity_footprint = alpha * E_h
    EV_industry_innovator_footprint = beta * E_h
    climate_skeptical_politician_footprint = gamma * E_h

    illustrative_actors_footprint = (
        climate_advocate_celebrity_footprint
        + EV_industry_innovator_footprint
        + climate_skeptical_politician_footprint
    )


    # Ordinary and rich households' footprints

    ordinary_households_footprint = (
        (1 - Lambda) * H * E_h
    )

    rich_households_footprint = (
        (Lambda * H - 3) * m_e * E_h
        + illustrative_actors_footprint
    )


    # Consumer role

    consumer_role = (
        rich_households_footprint
        + ordinary_households_footprint
    )


    # Voter role

    voter_role = R_v0 - R_inf_CA


    # Politician role

    politician_role = R_p0 * voter_role


    # Firm-manager role

    firm_manager_role = R_f0 * politician_role


    # Domestic and non-domestic consumption

    domestic_households_consumption = (
        politician_role
        * firm_manager_role
        * theta_d
        * consumer_role
    )

    non_domestic_households_consumption = (
        politician_role
        * theta_nd
        * consumer_role
    )


    # Total emissions

    emissions = (
        domestic_households_consumption
        + non_domestic_households_consumption
    )

    return emissions


# In[9]:


emissions_s3 = scenario_3(
    E_h, H, Lambda, m_e,
    alpha, beta, gamma,
    theta_d, theta_nd,
    R_v0, R_p0, R_f0,
    R_inf_CA
)
print(emissions_s3)


# In[10]:


# The climate-advocate celebrity's non-consumptive contribution

climate_advocate_celebrity_non_consumptive_effect = (
    emissions_s3 - emissions_s2
)

print(climate_advocate_celebrity_non_consumptive_effect)


# In[11]:


# The climate-advocate celebrity's footpirnt

climate_advocate_celebrity_footprint = alpha * E_h

print(climate_advocate_celebrity_footprint)


# The climate-advocate celebrity's lifeprint

climate_advocate_celebrity_lifeprint = (
    climate_advocate_celebrity_footprint
    + climate_advocate_celebrity_non_consumptive_effect
)


print(climate_advocate_celebrity_non_consumptive_effect)

print( climate_advocate_celebrity_lifeprint)


# Scenario 4:

# In[12]:


def scenario_4(
    E_h, H, Lambda, m_e,
    alpha, beta, gamma,
    theta_d, theta_nd,
    R_v0, R_p0, R_f0,
    n_EV_sell, n_EV_pro,
    E_r, E_ext,
    delta, sigma,
    m_1, m_2,
    p
):

    # Illustrative ultra-rich actors' footprints

    climate_advocate_celebrity_footprint = alpha * E_h
    EV_industry_innovator_footprint = beta * E_h
    climate_skeptical_politician_footprint = gamma * E_h

    illustrative_actors_footprint = (
        climate_advocate_celebrity_footprint
        + EV_industry_innovator_footprint
        + climate_skeptical_politician_footprint
    )


    # Ordinary and rich households' footprints

    ordinary_households_footprint = (
        (1 - Lambda) * H * E_h
    )

    rich_households_footprint = (
        (Lambda * H - 3) * m_e * E_h
        + illustrative_actors_footprint
    )


    # Consumer role

    consumer_role = (
        rich_households_footprint
        + ordinary_households_footprint
    )


    # Voter role

    voter_role = R_v0


    # Politician role

    politician_role = R_p0 * voter_role


    # Firm-manager role

    firm_manager_role = R_f0 * politician_role


    # EV market expansion multiplier

    if politician_role <= p:
        ev_market_expansion_multiplier = m_1
    else:
        ev_market_expansion_multiplier = m_2


    # EV driving emissions saving

    if politician_role <= p:
        ev_driving_emissions_savings = (
            n_EV_sell * E_r / 1_000_000
        )
    else:
        ev_driving_emissions_savings = (
            n_EV_sell
            * (1 - sigma)
            * E_r
            / 1_000_000
        )


    # EV impact on consumption

    ev_impact_on_consumption = (
        ev_driving_emissions_savings
        * ev_market_expansion_multiplier
    )


    # Extra emissions from EV production

    if politician_role <= p:
        extra_emissions_from_ev_production = (
            n_EV_pro * E_ext / 1_000_000
        )
    else:
        extra_emissions_from_ev_production = (
            n_EV_pro
            * (1 - delta)
            * E_ext
            / 1_000_000
        )


    # Domestic and non-domestic consumption

    domestic_households_consumption = (
        politician_role
        * firm_manager_role
        * theta_d
        * consumer_role
        - ev_impact_on_consumption
        + extra_emissions_from_ev_production
    )

    non_domestic_households_consumption = (
        politician_role
        * theta_nd
        * consumer_role
    )


    # Total emissions

    emissions = (
        domestic_households_consumption
        + non_domestic_households_consumption
    )

    return emissions


# In[13]:


emissions_s4 = scenario_4(
    E_h,
    H,
    Lambda,
    m_e,
    alpha,
    beta,
    gamma,
    theta_d,
    theta_nd,
    R_v0,
    R_p0,
    R_f0,
    n_EV_sell,
    n_EV_pro,
    E_r,
    E_ext,
    delta,
    sigma,
    m_1,
    m_2,
    p
)

print(emissions_s4)


# In[14]:


# The EV-industry innovator's non-consumptive contribution

EV_industry_innovator_non_consumptive_effect = (
    emissions_s4 - emissions_s2
)

print(EV_industry_innovator_non_consumptive_effect)


# In[15]:


# EV-industry innovator's footprint

EV_industry_innovator_footprint = beta * E_h

print (EV_industry_innovator_footprint)

# EV-industry innovator's lifeprint

EV_industry_innovator_lifeprint = (
    EV_industry_innovator_footprint
    + EV_industry_innovator_non_consumptive_effect
)

print(EV_industry_innovator_lifeprint)


# Scenario 5:

# In[16]:


def scenario_5(
    E_h, H, Lambda, m_e,
    alpha, beta, gamma,
    theta_d, theta_nd,
    R_v0_CS, R_p0, R_f0,
    v, S_p
):

    # Illustrative ultra-rich actors' footprints

    climate_advocate_celebrity_footprint = alpha * E_h
    EV_industry_innovator_footprint = beta * E_h
    climate_skeptical_politician_footprint = gamma * E_h

    illustrative_actors_footprint = (
        climate_advocate_celebrity_footprint
        + EV_industry_innovator_footprint
        + climate_skeptical_politician_footprint
    )


    # Ordinary and rich households' footprints

    ordinary_households_footprint = (
        (1 - Lambda) * H * E_h
    )

    rich_households_footprint = (
        (Lambda * H - 3) * m_e * E_h
        + illustrative_actors_footprint
    )


    # Consumer role

    consumer_role = (
        rich_households_footprint
        + ordinary_households_footprint
    )


    # Voter role

    voter_role = R_v0_CS


    # Climate-skeptical presidenty effect

    if voter_role <= v:
        climate_skeptical_presidency_effect = 0
    else:
        climate_skeptical_presidency_effect = S_p


    # Politician role

    if climate_skeptical_presidency_effect <= 0:
        politician_role = R_p0 * voter_role
    else:
        politician_role = R_p0 + climate_skeptical_presidency_effect


    # Firm-manager role

    firm_manager_role = R_f0 * politician_role


    # Domestic and non-domestic consumption

    domestic_households_consumption = (
        politician_role
        * firm_manager_role
        * theta_d
        * consumer_role
    )

    non_domestic_households_consumption = (
        politician_role
        * theta_nd
        * consumer_role
    )


    # Total emissions

    emissions = (
        domestic_households_consumption
        + non_domestic_households_consumption
    )

    return emissions


# In[17]:


emissions_s5 = scenario_5(
    E_h,
    H,
    Lambda,
    m_e,
    alpha,
    beta,
    gamma,
    theta_d,
    theta_nd,
    R_v0_CS,
    R_p0,
    R_f0,
    v,
     S_p
)

print(emissions_s5)


# In[18]:


# The climate-skeptical politician's non-consumptive contribution

climate_skeptical_politician_non_consumptive_effect = (
    emissions_s5 - emissions_s2
)

print(climate_skeptical_politician_non_consumptive_effect)


# In[19]:


# The climate-skeptical politician's footprint

climate_skeptical_politician_footprint = gamma * E_h

print(climate_skeptical_politician_footprint)

# The climate-skeptical politician's lifeprint

climate_skeptical_politician_lifeprint = (
    climate_skeptical_politician_footprint
    + climate_skeptical_politician_non_consumptive_effect
)

print(climate_skeptical_politician_lifeprint)


# Scenario 6:

# In[20]:


def scenario_6(
    E_h, H, Lambda, m_e,
    alpha, beta, gamma,
    theta_d, theta_nd,
    R_v0_CS, R_p0, R_f0,
    v, 
    n_EV_sell, n_EV_pro,
    E_r, E_ext,
    delta, sigma,
    m_1, m_2,
    p, S_p
):

    # Illustrative ultra-rich actors' footprints

    climate_advocate_celebrity_footprint = alpha * E_h
    EV_industry_innovator_footprint = beta * E_h
    climate_skeptical_politician_footprint = gamma * E_h

    illustrative_actors_footprint = (
        climate_advocate_celebrity_footprint
        + EV_industry_innovator_footprint
        + climate_skeptical_politician_footprint
    )


    # Ordinary and rich households' footprints

    ordinary_households_footprint = (
        (1 - Lambda) * H * E_h
    )

    rich_households_footprint = (
        (Lambda * H - 3) * m_e * E_h
        + illustrative_actors_footprint
    )


    # Consumer role

    consumer_role = (
        rich_households_footprint
        + ordinary_households_footprint
    )


    # Voter role

    voter_role = R_v0_CS


    # Climate-skeptical presidency

    if voter_role <= v:
        climate_skeptical_presidency_effect = 0
    else:
        climate_skeptical_presidency_effect = S_p


    # Politician role

    if climate_skeptical_presidency_effect <= 0:
        politician_role = R_p0 * voter_role
    else:
        politician_role = R_p0 + climate_skeptical_presidency_effect


    # Firm-manager role

    firm_manager_role = R_f0 * politician_role


    # EV market expansion multiplier

    if politician_role <= p:
        ev_market_expansion_multiplier = m_1
    else:
        ev_market_expansion_multiplier = m_2


    # EV driving emissions saving

    if politician_role <= p:
        ev_driving_emissions_savings = (
            n_EV_sell * E_r / 1_000_000
        )
    else:
        ev_driving_emissions_savings = (
            n_EV_sell
            * (1 - sigma)
            * E_r
            / 1_000_000
        )


    # EV impact on consumption

    ev_impact_on_consumption = (
        ev_driving_emissions_savings
        * ev_market_expansion_multiplier
    )


    # Extra emissions from EV production

    if politician_role <= p:
        extra_emissions_from_ev_production = (
            n_EV_pro * E_ext / 1_000_000
        )
    else:
        extra_emissions_from_ev_production = (
            n_EV_pro
            * (1 - delta)
            * E_ext
            / 1_000_000
        )


    # Domestic and non-domestic consumption

    domestic_households_consumption = (
        politician_role
        * firm_manager_role
        * theta_d
        * consumer_role
        - ev_impact_on_consumption
        + extra_emissions_from_ev_production
    )

    non_domestic_households_consumption = (
        politician_role
        * theta_nd
        * consumer_role
    )


    # Total emissions

    emissions = (
        domestic_households_consumption
        + non_domestic_households_consumption
    )

    return emissions


# In[21]:


emissions_s6 = scenario_6(
    E_h,
    H,
    Lambda,
    m_e,
    alpha,
    beta,
    gamma,
    theta_d,
    theta_nd,
    R_v0_CS,
    R_p0,
    R_f0,
    v,
    n_EV_sell,
    n_EV_pro,
    E_r,
    E_ext,
    delta,
    sigma,
    m_1,
    m_2,
    p, S_p
)

print(emissions_s6)


# In[22]:


# The joint non-consumptive contribution of the EV-industry innovator and the climate-skeptical politician

combined_non_consumptive_effect_skeptical_politician_EV_industry_innovator = (
    emissions_s6 - emissions_s2
)

print(combined_non_consumptive_effect_skeptical_politician_EV_industry_innovator)


# In[23]:


# The joint footprint of the EV-industry innovator and the climate-skeptical politician

combined_footprint_skeptical_politician_EV_industry_innovator = (
    EV_industry_innovator_footprint
    + climate_skeptical_politician_footprint
)

print(combined_footprint_skeptical_politician_EV_industry_innovator)


# The joint lifeprint of the EV-industry innovator and the climate-skeptical politician

joint_lifeprint_skeptical_politician_EV_industry_innovator = (
    combined_footprint_skeptical_politician_EV_industry_innovator
    + combined_non_consumptive_effect_skeptical_politician_EV_industry_innovator)

print (joint_lifeprint_skeptical_politician_EV_industry_innovator)


# In[ ]:





# Sensitivity analysis - One at a time (OAT)

# In[24]:


# Sensitivity analysis for parameter m_1
# range: m_1 = [1,3]
#influenced scenario: Scenario 4

m_1_values = np.linspace(1, 3, 21)

m_1_results = []

for m_1_test in m_1_values:

    emissions_s4_test = scenario_4(
        E_h,
        H,
        Lambda,
        m_e,
        alpha,
        beta,
        gamma,
        theta_d,
        theta_nd,
        R_v0,
        R_p0,
        R_f0,
        n_EV_sell,
        n_EV_pro,
        E_r,
        E_ext,
        delta,
        sigma,
        m_1_test,
        m_2,
        p
    )


    m_1_results.append([
        m_1_test,
        emissions_s4_test,
        emissions_s4_test - emissions_s2
    ])

# Table:

m_1_results_df = pd.DataFrame(
    m_1_results,
    columns=[
        "m_1",
        "Scenario_4_emissions",
        "E4_minus_E2"
    ]
)



m_1_results_df

print (m_1_results_df)


# Plot: 

plt.figure(figsize=(7, 5))


plt.plot(
    m_1_results_df["m_1"],
    m_1_results_df["E4_minus_E2"],
    linewidth=2
)


plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.axvline(
    x=m_1,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    m_1,
    emissions_s4 - emissions_s2,
    color="black",
    s=50,
    zorder=3,
    label="Baseline"
)

plt.xlabel("EV market expansion multiplier ($m_1$)")
plt.ylabel("EV-industry innovator's lifeprint")
plt.title("OAT sensitivity analysis for $m_1$")


plt.grid(alpha=0.25)

plt.tight_layout()
plt.show()


# In[25]:


# Sensitivity analysis for parameter m_2
# range: m_2 = [0.5,1.5]
#influenced scenario: Scenario 6

m_2_values = np.linspace(0.5, 1.5, 21)

m_2_results = []

for m_2_test in m_2_values:

    emissions_s6_test = scenario_6(
        E_h,
        H,
        Lambda,
        m_e,
        alpha,
        beta,
        gamma,
        theta_d,
        theta_nd,
        R_v0_CS,
        R_p0,
        R_f0,
        v,
        n_EV_sell,
        n_EV_pro,
        E_r,
        E_ext,
        delta,
        sigma,
        m_1,
        m_2_test,
        p,
        S_p
    )



    m_2_results.append([
        m_2_test,
        emissions_s6_test,
        emissions_s6_test - emissions_s2
    ])


# Table:

m_2_results_df = pd.DataFrame(
    m_2_results,
    columns=[
        "m_2",
        "Scenario_6_emissions",
        "E6_minus_E2"
    ]
)

m_2_results_df

print(m_2_results_df)


# Plot:

plt.figure(figsize=(7, 5))


plt.plot(
    m_2_results_df["m_2"],
    m_2_results_df["E6_minus_E2"],
    linewidth=2
)


plt.axvline(
    x=m_2,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    m_2,
    emissions_s6 - emissions_s2,
    color="black",
    s=50,
    zorder=3,
    label="Baseline"
)

plt.xlabel("EV market expansion multiplier ($m_2$)")
plt.ylabel(
    "Joint lifeprint"
)

plt.title(
    "Sensitivity of joint climate lifeprint to $m_2$"
)


plt.grid(alpha=0.25)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.tight_layout()
plt.show()


# In[26]:


# Sensitivity analysis for parameter p
# range: p = [0.5,2]
#influenced scenario: Scenarios 4 and 6

p_values = np.linspace(0.5, 2.0, 151)

p_results = []

for p_test in p_values:

    # Scenario 4
    emissions_s4_test = scenario_4(
        E_h,
        H,
        Lambda,
        m_e,
        alpha,
        beta,
        gamma,
        theta_d,
        theta_nd,
        R_v0,
        R_p0,
        R_f0,
        n_EV_sell,
        n_EV_pro,
        E_r,
        E_ext,
        delta,
        sigma,
        m_1,
        m_2,
        p_test
    )

    # Scenario 6
    emissions_s6_test = scenario_6(
        E_h,
        H,
        Lambda,
        m_e,
        alpha,
        beta,
        gamma,
        theta_d,
        theta_nd,
        R_v0_CS,
        R_p0,
        R_f0,
        v,
        n_EV_sell,
        n_EV_pro,
        E_r,
        E_ext,
        delta,
        sigma,
        m_1,
        m_2,
        p_test,
        S_p
    )



    p_results.append([
        p_test,
        emissions_s4_test - emissions_s2,
        emissions_s6_test - emissions_s2
    ])


# Table:

p_results_df = pd.DataFrame(
    p_results,
    columns=[
        "p",
        "E4_minus_E2",
        "E6_minus_E2"
    ]
)

p_results_df

print(p_results_df)

# Plot for E4-E2

plt.figure(figsize=(7, 5))

plt.plot(
    p_results_df["p"],
    p_results_df["E4_minus_E2"],
    linewidth=2
)

plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    x=p,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    p,
    emissions_s4 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Politician role threshold ($p$)")
plt.ylabel(
    "EV-industry innovator's lifeprint"
)

plt.title(
    "Sensitivity of EV-industry innovator lifeprint to $p$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot E6-E2

plt.figure(figsize=(7, 5))

plt.plot(
    p_results_df["p"],
    p_results_df["E6_minus_E2"],
    linewidth=2
)

plt.axvline(
    x=p,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    p,
    emissions_s6 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Politician role threshold ($p$)")
plt.ylabel(
    "Joint lifeprint"
)

plt.title(
    "Sensitivity of joint climate lifeprint to $p$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# In[27]:


# Sensitivity analysis for parameter R_f0
# range: R_f0 = [0.6,1]
#influenced scenario: Scenarios 2, 3, 4, 5, 6

R_f0_values = np.linspace(0.6, 1.0, 21)

R_f0_results = []

for R_f0_test in R_f0_values:

    # Scenario 2
    emissions_s2_test = scenario_2(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0, R_p0, R_f0_test
    )

    # Scenario 3
    emissions_s3_test = scenario_3(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0, R_p0, R_f0_test,
        R_inf_CA
    )

    # Scenario 4
    emissions_s4_test = scenario_4(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0, R_p0, R_f0_test,
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta, sigma,
        m_1, m_2,
        p
    )

    # Scenario 5
    emissions_s5_test = scenario_5(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0, R_f0_test,
        v, S_p
    )

    # Scenario 6
    emissions_s6_test = scenario_6(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0, R_f0_test,
        v,
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta, sigma,
        m_1, m_2,
        p, S_p
    )



    R_f0_results.append([
        R_f0_test,
        emissions_s2_test - emissions_s1,
        emissions_s3_test - emissions_s2_test,
        emissions_s4_test - emissions_s2_test,
        emissions_s5_test - emissions_s2_test,
        emissions_s6_test - emissions_s2_test
    ])


# Table:

R_f0_results_df = pd.DataFrame(
    R_f0_results,
    columns=[
        "R_f0",
        "E2_minus_E1",
        "E3_minus_E2",
        "E4_minus_E2",
        "E5_minus_E2",
        "E6_minus_E2"
    ]
)

R_f0_results_df

print(R_f0_results_df)


#Plot:

# Plot for E2-E1

plt.figure(figsize=(7, 5))

plt.plot(
    R_f0_results_df["R_f0"],
    R_f0_results_df["E2_minus_E1"],
    linewidth=2
)

plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    x=R_f0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_f0,
    emissions_s2 - emissions_s1,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of firm-manager role ($R_{f0}$)")
plt.ylabel("Difference between societal climate lifeprint and carbon footprint ($E_2-E_1$)")

plt.title(
    "Sensitivity of the societal climate lifeprint–carbon footprint difference to $R_{f0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()



# Plot for E3-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_f0_results_df["R_f0"],
    R_f0_results_df["E3_minus_E2"],
    linewidth=2
)


plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.axvline(
    x=R_f0,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    R_f0,
    emissions_s3 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of firm-manager role ($R_{f0}$) ")
plt.ylabel(
    "Climate-advocate celebrity's lifeprint ($E_3-E_2$)"
)

plt.title(
    "Sensitivity of the climate-advocate celebrity lifeprint to $R_{f0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()



# Plot for E4-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_f0_results_df["R_f0"],
    R_f0_results_df["E4_minus_E2"],
    linewidth=2
)


plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.axvline(
    x=R_f0,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    R_f0,
    emissions_s4 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of firm-manager role ($R_{f0}$)")
plt.ylabel(
    "EV-industry innovator's lifeprint"
)

plt.title(
    "Sensitivity of EV-industry innovator's lifeprint to $R_{f0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()



# Plot for E5-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_f0_results_df["R_f0"],
    R_f0_results_df["E5_minus_E2"],
    linewidth=2
)


plt.axvline(
    x=R_f0,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    R_f0,
    emissions_s5 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of firm-manager role ($R_{f0}$)")
plt.ylabel(
    "Climate-skeptical politician's lifeprint ($E_5-E_2$)"
)

plt.title(
    "Sensitivity of the climate-skeptical politician's lifeprint to $R_{f0}$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


#Plot for E6-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_f0_results_df["R_f0"],
    R_f0_results_df["E6_minus_E2"],
    linewidth=2
)


plt.axvline(
    x=R_f0,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    R_f0,
    emissions_s6 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of firm-manager role ($R_{f0}$)")
plt.ylabel(
    "Joint climate lifeprint ($E_6-E_2$)"
)

plt.title(
    "Sensitivity of joint climate lifeprint to $R_{f0}$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# In[28]:


# Sensitivity analysis for parameter R_p0
# range: R_p0 = [0.5,0.9]
#influenced scenario: Scenarios 2, 3, 4, 5, 6

R_p0_values = np.linspace(0.5, 0.9, 21)

R_p0_results = []

for R_p0_test in R_p0_values:

    # Scenario 2
    emissions_s2_test = scenario_2(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0, R_p0_test, R_f0
    )

    # Scenario 3
    emissions_s3_test = scenario_3(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0, R_p0_test, R_f0,
        R_inf_CA
    )

    # Scenario 4
    emissions_s4_test = scenario_4(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0, R_p0_test, R_f0,
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta, sigma,
        m_1, m_2,
        p
    )

    # Scenario 5
    emissions_s5_test = scenario_5(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0_test, R_f0,
        v, S_p
    )

    # Scenario 6
    emissions_s6_test = scenario_6(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0_test, R_f0,
        v,
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta, sigma,
        m_1, m_2,
        p, S_p
    )

    R_p0_results.append([
        R_p0_test,
        emissions_s2_test - emissions_s1,
        emissions_s3_test - emissions_s2_test,
        emissions_s4_test - emissions_s2_test,
        emissions_s5_test - emissions_s2_test,
        emissions_s6_test - emissions_s2_test
    ])


# Table

R_p0_results_df = pd.DataFrame(
    R_p0_results,
    columns=[
        "R_p0",
        "E2_minus_E1",
        "E3_minus_E2",
        "E4_minus_E2",
        "E5_minus_E2",
        "E6_minus_E2"
    ]
)

R_p0_results_df

print (R_p0_results_df)


# Plot

# Plot for E2-E1

plt.figure(figsize=(7, 5))

plt.plot(
    R_p0_results_df["R_p0"],
    R_p0_results_df["E2_minus_E1"],
    linewidth=2
)

plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    x=R_p0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_p0,
    emissions_s2 - emissions_s1,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of politician role ($R_{p0}$)")
plt.ylabel(
    "Difference between societal climate lifeprint and carbon footprint ($E_2-E_1$)"
)

plt.title(
    "Sensitivity of societal climate lifeprint-carbon footprint difference to $R_{p0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot for E3-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_p0_results_df["R_p0"],
    R_p0_results_df["E3_minus_E2"],
    linewidth=2
)

plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    x=R_p0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_p0,
    emissions_s3 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of politician role ($R_{p0}$)")
plt.ylabel(
    "Climate-advocate celebrity's lifeprint ($E_3-E_2$)"
)

plt.title(
    "Sensitivity of climate-advocate celebrity's lifeprint to $R_{p0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot for the E4-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_p0_results_df["R_p0"],
    R_p0_results_df["E4_minus_E2"],
    linewidth=2
)

plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    x=R_p0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_p0,
    emissions_s4 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of politician role ($R_{p0}$)")
plt.ylabel(
    "EV-industry innovator's lifeprint"
)

plt.title(
    "Sensitivity of EV-industry innovator's lifeprint to $R_{p0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot for E5-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_p0_results_df["R_p0"],
    R_p0_results_df["E5_minus_E2"],
    linewidth=2
)

plt.axvline(
    x=R_p0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_p0,
    emissions_s5 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of politician role ($R_{p0}$)")
plt.ylabel(
    "Climate-skeptical politician's lifeprint ($E_5-E_2$), MtCO$_2$"
)

plt.title(
    "Sensitivity of climate-skeptical politician's lifeprint to $R_{p0}$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot for E6-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_p0_results_df["R_p0"],
    R_p0_results_df["E6_minus_E2"],
    linewidth=2
)

plt.axvline(
    x=R_p0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_p0,
    emissions_s6 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of politician role ($R_{p0}$)")
plt.ylabel(
    "Joint climate lifeprint ($E_6-E_2$), MtCO$_2$"
)

plt.title(
    "Sensitivity of joint climate lifeprint to $R_{p0}$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()




# In[29]:


# Sensitivity analysis for parameter R_v0
# range: R_v0 = [0.8,1.2]
#influenced scenario: Scenarios 2, 3, and 4

R_v0_values = np.linspace(0.8, 1.2, 81)

R_v0_results = []


for R_v0_test in R_v0_values:

    # Scenario 2
    emissions_s2_test = scenario_2(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_test, R_p0, R_f0
    )

    # Scenario 3
    emissions_s3_test = scenario_3(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_test, R_p0, R_f0,
        R_inf_CA
    )

    # Scenario 4
    emissions_s4_test = scenario_4(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_test, R_p0, R_f0,
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta, sigma,
        m_1, m_2,
        p
    )


    R_v0_results.append([
        R_v0_test,
        emissions_s2_test - emissions_s1,
        emissions_s3_test - emissions_s2_test,
        emissions_s4_test - emissions_s2_test
    ])


# Table:

R_v0_results_df = pd.DataFrame(
    R_v0_results,
    columns=[
        "R_v0",
        "E2_minus_E1",
        "E3_minus_E2",
        "E4_minus_E2"

    ]
)

R_v0_results_df

print (R_v0_results_df)



# Plot

# Plot for E2-E1

plt.figure(figsize=(7, 5))

plt.plot(
    R_v0_results_df["R_v0"],
    R_v0_results_df["E2_minus_E1"],
    linewidth=2
)

plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    x=R_v0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_v0,
    emissions_s2 - emissions_s1,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of voter role ($R_{v0}$)")
plt.ylabel(
    "Difference between societal climate lifeprint and carbon footprint ($E_2-E_1$)"
)

plt.title(
    "Sensitivity of societal climate lifeprint-carbon footprint difference to $R_{v0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot E3-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_v0_results_df["R_v0"],
    R_v0_results_df["E3_minus_E2"],
    linewidth=2
)

plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    x=R_v0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_v0,
    emissions_s3 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of voter role ($R_{v0}$)")
plt.ylabel(
    "Climate-advocate celebrity's lifeprint ($E_3-E_2$)"
)

plt.title(
    "Sensitivity of climate-advocate celebrity's lifeprint to $R_{v0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot for E4-E2

plt.figure(figsize=(7, 5))

plt.plot(
    R_v0_results_df["R_v0"],
    R_v0_results_df["E4_minus_E2"],
    linewidth=2
)

plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.axvline(
    x=R_v0,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.scatter(
    R_v0,
    emissions_s4 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Reference value of voter role ($R_{v0}$)")
plt.ylabel(
    "EV-industry innovator's lifeprint"
)

plt.title(
    "Sensitivity of EV-industry innovator's lifeprint to $R_{v0}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()




# In[30]:


# Sensitivity analysis for parameter R_v0_CS
# range: R_v0_cs = [1.01,1.20]
#influenced scenario: Scenarios 5 and 6


R_v0_CS_values = np.linspace(1.01, 1.20, 20)

R_v0_CS_results = []


for R_v0_CS_test in R_v0_CS_values:

    # Scenario 5
    emissions_s5_test = scenario_5(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS_test, R_p0, R_f0,
        v,
        S_p
    )

    # Scenario 6
    emissions_s6_test = scenario_6(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS_test, R_p0, R_f0,
        v,
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta, sigma,
        m_1, m_2,
        p, S_p
    )

    R_v0_CS_results.append([
        R_v0_CS_test,
        emissions_s5_test - emissions_s2,
        emissions_s6_test - emissions_s2
    ])


# Table

R_v0_CS_results_df = pd.DataFrame(
    R_v0_CS_results,
    columns=[
        "R_v0_CS",
        "E5_minus_E2",
        "E6_minus_E2"
    ]
)

R_v0_CS_results_df

print(R_v0_CS_results_df)

# Plot for E5-E2

plt.figure(figsize=(8, 5))

plt.plot(
    R_v0_CS_results_df["R_v0_CS"],
    R_v0_CS_results_df["E5_minus_E2"]
)


baseline_E5 = R_v0_CS_results_df.loc[
    np.isclose(R_v0_CS_results_df["R_v0_CS"], 1.10),
    "E5_minus_E2"
].iloc[0]

plt.scatter(1.10, baseline_E5, color="black", zorder=3)


plt.axvline(
    x=1.10,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.xlabel(r"Reference value of voter role ($R_{v0}^{CS}$)")
plt.ylabel(r"Climate-skeptical politician's lifeprint")
plt.title(
    r"Sensitivity of climate-skeptical politician's lifeprint to $R_{v0}^{CS}$"
)

plt.ticklabel_format(style="plain", axis="y", useOffset=False)
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot for E6-E2

plt.figure(figsize=(8, 5))

plt.plot(
    R_v0_CS_results_df["R_v0_CS"],
    R_v0_CS_results_df["E6_minus_E2"]
)


baseline_E6 = R_v0_CS_results_df.loc[
    np.isclose(R_v0_CS_results_df["R_v0_CS"], 1.10),
    "E6_minus_E2"
].iloc[0]

plt.scatter(1.10, baseline_E6, color="black", zorder=3)


plt.axvline(
    x=1.10,
    color="gray",
    linestyle="--",
    linewidth=1
)

plt.xlabel(r"Reference value of  voter role ($R_{v0}^{CS}$)")
plt.ylabel(r"Joint lifeprint")
plt.title(
    r"Sensitivity of joint climate lifeprint to $R_{v0}^{CS}$"
)

plt.ticklabel_format(style="plain", axis="y", useOffset=False)
plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()




# In[31]:


# Sensitivity analysis for parameter S_p
# range: S_p = [0.5,1.5]
#influenced scenario: Scenarios 5 and 6

S_p_values = np.linspace(0.5, 1.5, 21)

S_p_results = []

for S_p_test in S_p_values:

    # Scenario 5
    emissions_s5_test = scenario_5(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0, R_f0,
        v,  S_p_test
    )

    # Scenario 6
    emissions_s6_test = scenario_6(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0, R_f0,
        v,
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta, sigma,
        m_1, m_2,
        p, S_p_test
    )

    S_p_results.append([
        S_p_test,
        emissions_s5_test - emissions_s2,
        emissions_s6_test - emissions_s2
    ])


# Table:

S_p_results_df = pd.DataFrame(
    S_p_results,
    columns=[
        "S_p",
        "E5_minus_E2",
        "E6_minus_E2"
    ]
)

S_p_results_df

print (S_p_results_df)



# Plot E5-E2

plt.figure(figsize=(7, 5))

plt.plot(
    S_p_results_df["S_p"],
    S_p_results_df["E5_minus_E2"],
    linewidth=2
)


plt.axvline(
    x=S_p,
    color="gray",
    linestyle="--",
    linewidth=1
)

# Baseline result
plt.scatter(
    S_p,
    emissions_s5 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Climate-skeptical presidency effect ($S_p$)")
plt.ylabel(
    "Climate-skeptical politician's lifeprint ($E_5-E_2$)"
)

plt.title(
    "Sensitivity of the climate-skeptical politician's lifeprint to $S_p$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot for E6-E2

plt.figure(figsize=(7, 5))

plt.plot(
    S_p_results_df["S_p"],
    S_p_results_df["E6_minus_E2"],
    linewidth=2
)


plt.axvline(
    x=S_p,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    S_p,
    emissions_s6 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Climate-skeptical presidency effect ($S_p$)")
plt.ylabel(
    "Joint climate lifeprint ($E_6-E_2$)"
)

plt.title(
    "Sensitivity of joint climate lifeprint to $S_p$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# In[37]:


# Sensitivity analysis for parameter v
# range: v = [0.8,1.2]
#influenced scenario: Scenarios 5 and 6

v_values = np.linspace(0.8, 1.2, 81)

v_results = []

for v_test in v_values:

    # Scenario 5
    emissions_s5_test = scenario_5(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0, R_f0,
        v_test,  S_p
    )

    # Scenario 6
    emissions_s6_test = scenario_6(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0, R_f0,
        v_test, 
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta, sigma,
        m_1, m_2,
        p, S_p
    )

    v_results.append([
        v_test,
        emissions_s5_test - emissions_s2,
        emissions_s6_test - emissions_s2
    ])


# Table:

v_results_df = pd.DataFrame(
    v_results,
    columns=[
        "v",
        "E5_minus_E2",
        "E6_minus_E2"
    ]
)

v_results_df

print(v_results_df)


# Plot E5-E2

plt.figure(figsize=(7, 5))

plt.plot(
    v_results_df["v"],
    v_results_df["E5_minus_E2"],
    linewidth=2
)

# Baseline v
plt.axvline(
    x=v,
    color="gray",
    linestyle="--",
    linewidth=1
)

# Baseline result
plt.scatter(
    v,
    emissions_s5 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Voter role threshold ($v$)")
plt.ylabel(
    "Climate-sceptical politician's lifeprint"
)

plt.title(
    "Sensitivity of climate-sceptical politician's lifeprint to $v$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# Plot for E6-E2

plt.figure(figsize=(7, 5))

plt.plot(
    v_results_df["v"],
    v_results_df["E6_minus_E2"],
    linewidth=2
)

# Baseline v
plt.axvline(
    x=v,
    color="gray",
    linestyle="--",
    linewidth=1
)

# Baseline result
plt.scatter(
    v,
    emissions_s6 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel("Voter role threshold ($v$)")
plt.ylabel(
    "Joint lifeprint"
)

plt.title(
    "Sensitivity of joint climate lifeprint to $v$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# In[33]:


# Sensitivity analysis for parameter R_inf,CA
# range: R_inf,AC = [0.01,0.06]
#influenced scenario: Scenario 3

R_infCA_values = np.linspace(0.01, 0.06, 21)

R_infCA_results = []

for R_infCA_test in R_infCA_values:

    emissions_s3_test = scenario_3(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0, R_p0, R_f0,
        R_infCA_test
    )



    R_infCA_results.append([
        R_infCA_test,
        emissions_s3_test,
        emissions_s3_test - emissions_s2
    ])


# Table:

R_infCA_results_df = pd.DataFrame(
    R_infCA_results,
    columns=[
        "R_inf_CA",
        "Scenario_3_emissions",
        "E3_minus_E2"
    ]
)

R_infCA_results_df

print (R_infCA_results_df)




# Plot

plt.figure(figsize=(7, 5))

plt.plot(
    R_infCA_results_df["R_inf_CA"],
    R_infCA_results_df["E3_minus_E2"],
    linewidth=2
)


plt.axhline(
    y=0,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.axvline(
    x=R_inf_CA,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    R_inf_CA,
    emissions_s3 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel(
    "Climate-advocate celebrity's social influence ($R_{inf,CA}$)"
)

plt.ylabel(
    "Climate-advocate celebrity's lifeprint ($E_3-E_2$)"
)

plt.title(
    "Sensitivity of climate-advocate celebrity's lifeprint to $R_{inf,CA}$"
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()



# In[34]:


# Sensitivity analysis for parameter δ
# range: δ = [0.3,0.6]
#influenced scenario: Scenario 6

delta_values = np.linspace(0.30, 0.60, 31)

delta_results = []

for delta_test in delta_values:

    emissions_s6_test = scenario_6(
        E_h, H, Lambda, m_e,
        alpha, beta, gamma,
        theta_d, theta_nd,
        R_v0_CS, R_p0, R_f0,
        v,
        n_EV_sell, n_EV_pro,
        E_r, E_ext,
        delta_test, sigma,
        m_1, m_2,
        p, S_p
    )



    delta_results.append([
        delta_test,
        emissions_s6_test,
        emissions_s6_test - emissions_s2
    ])


# Table:

delta_results_df = pd.DataFrame(
    delta_results,
    columns=[
        "delta",
        "Scenario_6_emissions",
        "E6_minus_E2"
    ]
)

delta_results_df

print (delta_results_df)



# Plot:

plt.figure(figsize=(7, 5))

plt.plot(
    delta_results_df["delta"],
    delta_results_df["E6_minus_E2"],
    linewidth=2
)


plt.axvline(
    x=delta,
    color="gray",
    linestyle="--",
    linewidth=1
)


plt.scatter(
    delta,
    emissions_s6 - emissions_s2,
    color="black",
    s=50,
    zorder=3
)

plt.xlabel(
    "Reduction in EV production under climate-skeptical policy ($\\delta$)"
)

plt.ylabel(
    "Joint climate lifeprint ($E_6-E_2$)"
)

plt.title(
    "Sensitivity of joint climate lifeprint to $\\delta$"
)

plt.ticklabel_format(
    style="plain",
    axis="y",
    useOffset=False
)

plt.grid(alpha=0.25)
plt.tight_layout()
plt.show()


# In[36]:


# Tornado plot for continuous parameters m_1, m_2, R_f0, R_p0, R_inf,AC, S_p

def make_tornado(parameter_results, baseline_output, title):

    tornado_data = []

    for parameter_name, df, output_column in parameter_results:


        output_min = df[output_column].min()
        output_max = df[output_column].max()


        change_min = (
            (output_min - baseline_output)
            / abs(baseline_output)
            * 100
        )

        change_max = (
            (output_max - baseline_output)
            / abs(baseline_output)
            * 100
        )

        tornado_data.append([
            parameter_name,
            change_min,
            change_max
        ])

    tornado_df = pd.DataFrame(
        tornado_data,
        columns=[
            "Parameter",
            "Minimum_change",
            "Maximum_change"
        ]
    )


    tornado_df["Sensitivity"] = tornado_df[
        ["Minimum_change", "Maximum_change"]
    ].abs().max(axis=1)


    tornado_df = tornado_df.sort_values(
        "Sensitivity",
        ascending=True
    )


    tornado_df["Width"] = (
        tornado_df["Maximum_change"]
        - tornado_df["Minimum_change"]
    )

    plt.figure(figsize=(8, 5))

    plt.barh(
        tornado_df["Parameter"],
        tornado_df["Width"],
        left=tornado_df["Minimum_change"]
    )


    plt.axvline(
        x=0,
        color="black",
        linestyle="--",
        linewidth=1
    )

    plt.xlabel("Change from baseline outcome (%)")
    plt.title(title)

    plt.grid(
        axis="x",
        alpha=0.25
    )

    plt.tight_layout()
    plt.show()

    return tornado_df



# Tornado plot for E2 - E1

tornado_E2_E1 = make_tornado(
    [
        ("$R_{f0}$", R_f0_results_df, "E2_minus_E1"),
        ("$R_{p0}$", R_p0_results_df, "E2_minus_E1"),
        ("$R_{v0}$", R_v0_results_df, "E2_minus_E1")
    ],

    baseline_output=emissions_s2 - emissions_s1,

    title="Sensitivity of societal climate lifeprint–carbon footprint difference"
)



# Tornado plot for E3 - E2


tornado_E3 = make_tornado(
    [
        (
            "$R_{f0}$",
            R_f0_results_df,
            "E3_minus_E2"
        ),
        (
            "$R_{p0}$",
            R_p0_results_df,
            "E3_minus_E2"
        ),


        (
            "$R_{v0}$",
            R_v0_results_df,
            "E3_minus_E2"
        ),

        (
            "$R_{inf,CA}$",
            R_infCA_results_df,
            "E3_minus_E2"
        )
    ],

    baseline_output=emissions_s3 - emissions_s2,

    title=(
        "Sensitivity of climate-advocate celebrity's lifeprint"
    )
)



# Tornado plot for E4 - E2

tornado_E4 = make_tornado(
    [
        (
            "$m_1$",
            m_1_results_df,
            "E4_minus_E2"
        ),
       # (
            #"$R_{f0}$",
           # R_f0_results_df,
           # "E4_minus_E2"
       # ),
       # (
       #     "$R_{p0}$",
       #     R_p0_results_df,
       #     "E4_minus_E2"
       # ),


       # (
          #  "$R_{v0}$",
         #   R_v0_results_df,
          #  "E4_minus_E2"
       # )
    ],

    baseline_output=emissions_s4 - emissions_s2,

    title=(
        "Sensitivity of EV-industry innovator lifeprint"
    )
)


# Tornado plot for E5 - E2


tornado_E5 = make_tornado(
    [
        (
            "$R_{f0}$",
            R_f0_results_df,
            "E5_minus_E2"
        ),
        (
            "$R_{p0}$",
            R_p0_results_df,
            "E5_minus_E2"
        ),
        (
            "$S_p$",
            S_p_results_df,
            "E5_minus_E2"
        ),
       # (
         #   "$R_{v0}^{CS}$",
        #    R_v0_CS_results_df,
        #    "E5_minus_E2"
       # )
    ],

    baseline_output=emissions_s5 - emissions_s2,

    title=(
        "Sensitivity of climate-skeptical politician lifeprint"
    )
)

# Tornado plot for E6 - E2


tornado_E6 = make_tornado(
    [

        (
            "$R_{f0}$",
            R_f0_results_df,
            "E6_minus_E2"
        ),
        (
            "$R_{p0}$",
            R_p0_results_df,
            "E6_minus_E2"
        ),
        (
            "$S_p$",
            S_p_results_df,
            "E6_minus_E2"
        ),

    ],

    baseline_output=emissions_s6 - emissions_s2,

    title=(
        "Sensitivity of joint climate lifeprint"
    )
)



# In[ ]:





# In[ ]:





# In[ ]:




