
from flask import Flask, render_template

import os

app = Flask(__name__)

app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "False").lower() == "true"


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RabbiCode | Intelligent Data Solutions</title>

        <style>
* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f9fc;
    color: #172033;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 22px 8%;
    background: #ffffff;
    border-bottom: 1px solid #e8edf5;
}

.logo {
    font-size: 26px;
    font-weight: bold;
    color: #1746a2;
    letter-spacing: -0.5px;
}

nav a {
    margin-left: 26px;
    color: #334155;
    text-decoration: none;
    font-size: 15px;
    transition: color 0.2s ease;
}

nav a:hover {
    color: #2563eb;
}

.hero {
    padding: 110px 8%;
    background: linear-gradient(120deg, #10254a, #173d73);
    color: white;
}

.hero h1 {
    max-width: 750px;
    font-size: 50px;
    line-height: 1.15;
    letter-spacing: -1.2px;
    margin-bottom: 24px;
}

.hero p {
    max-width: 600px;
    font-size: 18px;
    line-height: 1.8;
    color: #dbe5f5;
}

.button {
    display: inline-block;
    margin-top: 22px;
    padding: 15px 26px;
    background: #4f8cff;
    color: white;
    text-decoration: none;
    font-weight: bold;
    border-radius: 7px;
    transition: background 0.2s ease, transform 0.2s ease;
}

.button:hover {
    background: #3675e8;
    transform: translateY(-2px);
}

.services {
    padding: 75px 8%;
}

.services h2 {
    font-size: 34px;
    letter-spacing: -0.5px;
}

.service-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 24px;
    margin-top: 32px;
}

.service-card {
    background: white;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 15px rgba(23, 32, 51, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.service-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 14px 30px rgba(23, 32, 51, 0.10);
}

.service-card h3 {
    color: #1746a2;
    font-size: 21px;
}

.service-card p {
    line-height: 1.8;
    color: #526078;
}

.service-card .package-price {
    color: #172033;
    font-size: 30px;
    margin: 18px 0;
}

.package-note {
    color: #526078;
    font-size: 14px;
    line-height: 1.7;
}

#pricing .service-card {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

#pricing .service-card .button {
    margin-top: auto;
}

#pricing .service-card p {
    margin: 9px 0;
}

#pricing .service-card hr {
    width: 100%;
    border: 0;
    border-top: 1px solid #e2e8f0;
    margin: 16px 0;
}

.contact-buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 22px;
}

.whatsapp-button {
    background: #25D366;
}

.whatsapp-button:hover {
    background: #1eae54;
}

footer {
    padding: 30px 8%;
    text-align: center;
    background: #10254a;
    color: #e2eaf8;
    line-height: 1.8;
}

@media (max-width: 900px) {
    .service-grid {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 42px;
    }
}

@media (max-width: 700px) {
    nav {
        flex-direction: column;
        gap: 18px;
    }

    nav a {
        margin: 0 8px;
    }

    .hero {
        padding: 70px 8%;
    }

    .hero h1 {
        font-size: 36px;
    }

    .hero p {
        font-size: 16px;
    }

    .services {
        padding: 50px 8%;
    }
}
        </style>
    </head>

    <body>

        <!-- Navigation -->
        <nav>
            <div class="logo">RabbiCode</div>

            <div>
                <a href="#home">Home</a>
                <a href="#services">Services</a>
                <a href="#pricing">Pricing</a>
                <a href="#contact">Contact</a>
                <a href="/dashboard">Sales Dashboard</a>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="hero" id="home">
            <h1>Turn Your Business Data Into Better Decisions.</h1>

            <p>
                RabbiCode helps businesses understand their sales,
                customers, and performance through data analytics
                and business intelligence.
            </p>

            <a class="button" href="#services">
                Explore Our Services
            </a>
        </section>

        <!-- Services Section -->
        <section class="services" id="services">
            <h2>What We Do</h2>

            <div class="service-grid">

                <div class="service-card">
                    <h3>Sales Analytics</h3>
                    <p>
                        Understand revenue trends, product performance,
                        and opportunities to improve sales.
                    </p>
                </div>

                <div class="service-card">
                    <h3>Business Intelligence</h3>
                    <p>
                        Transform business data into clear reports,
                        dashboards, and actionable insights.
                    </p>
                </div>

                <div class="service-card">
                    <h3>Customer Analytics</h3>
                    <p>
                        Discover customer behaviour, buying patterns,
                        and opportunities to improve retention.
                    </p>
                </div>

            </div>
        </section>

        <!-- Pricing Section -->
        <section class="services" id="pricing">
            <h2>Sales Analytics Packages</h2>

            <p>
                Choose a package that suits your business needs.
                RabbiCode helps you turn sales data into better decisions.
            </p>

            <p class="package-note">
                Introductory one-time project fees. Final scope will
                be agreed upon before work begins.
            </p>

            <div class="service-grid">

                <!-- Basic Package -->
                <div class="service-card">
                    <h3>Basic</h3>

                    <h2 class="package-price">₦40,000</h2>

                    <p>
                        <strong>
                            Get a clear picture of your business sales,
                            revenue and product performance.
                        </strong>
                    </p>

                    <hr>

                    <p>✓ Sales performance summary</p>
                    <p>✓ Revenue and order analysis</p>
                    <p>✓ Top-selling products analysis</p>
                    <p>✓ PDF report with charts</p>

                    <a class="button"
                       href="https://wa.me/2348147170033?text=Hello%20RabbiCode%2C%20I%20am%20interested%20in%20the%20Basic%20Sales%20Analytics%20Package."
                       target="_blank"
                       rel="noopener noreferrer">
                        Get Started
                    </a>
                </div>

                <!-- Standard Package -->
                <div class="service-card"
                     style="border: 2px solid #2563eb;">

                    <p style="color: #2563eb; font-weight: bold;">
                        MOST POPULAR
                    </p>

                    <h3>Standard</h3>

                    <h2 class="package-price">₦85,000</h2>

                    <p>
                        <strong>
                            Track your business performance with
                            interactive dashboards and actionable
                            sales insights.
                        </strong>
                    </p>

                    <hr>

                    <p>✓ Everything in Basic</p>
                    <p>✓ Interactive sales dashboard</p>
                    <p>✓ Monthly sales trends</p>
                    <p>✓ Product performance analysis</p>
                    <p>✓ Business insights and recommendations</p>

                    <a class="button"
                       href="https://wa.me/2348147170033?text=Hello%20RabbiCode%2C%20I%20am%20interested%20in%20the%20Standard%20Sales%20Analytics%20Package."
                       target="_blank"
                       rel="noopener noreferrer">
                        Get Started
                    </a>
                </div>

                <!-- Premium Package -->
                <div class="service-card">
                    <h3>Premium</h3>

                    <h2 class="package-price">₦160,000</h2>

                    <p>
                        <strong>
                            Unlock deeper sales and customer insights
                            with advanced analytics, forecasting and
                            strategic recommendations.
                        </strong>
                    </p>

                    <hr>

                    <p>✓ Everything in Standard</p>
                    <p>✓ Advanced sales analysis</p>
                    <p>✓ Customer and product performance</p>
                    <p>✓ Sales forecasting where appropriate</p>
                    <p>✓ Management report</p>
                    <p>✓ One month of post-delivery support</p>

                    <a class="button"
                       href="https://wa.me/2348147170033?text=Hello%20RabbiCode%2C%20I%20am%20interested%20in%20the%20Premium%20Sales%20Analytics%20Package."
                       target="_blank"
                       rel="noopener noreferrer">
                        Get Started
                    </a>
                </div>

            </div>
        </section>

        <!-- Contact Section -->
        <section class="services" id="contact">
            <h2>Let's Talk About Your Business Data</h2>

            <p>
                Have questions about your sales, customers, or business
                performance? Contact RabbiCode to discuss how data analytics
                can help your business.
            </p>

            <div class="contact-buttons">

                <a class="button"
                   href="https://mail.google.com/mail/?view=cm&fs=1&to=dennis.ugwuonu@gmail.com"
                   target="_blank"
                   rel="noopener noreferrer">
                    Email RabbiCode
                </a>

                <a class="button whatsapp-button"
                   href="https://wa.me/2348147170033?text=Hello%20RabbiCode%2C%20I%20would%20like%20to%20discuss%20your%20data%20analytics%20services."
                   target="_blank"
                   rel="noopener noreferrer">
                    Chat with RabbiCode on WhatsApp
                </a>

            </div>
        </section>

        <!-- Footer -->
        <footer>
            <p>RabbiCode | Intelligent Data Solutions for Businesses</p>
            <p>Helping businesses make data-informed decisions.</p>
            <p>&copy; 2026 RabbiCode. All rights reserved.</p>
        </footer>

    </body>
    </html>
    """


# Sales Dashboard Route
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run()
