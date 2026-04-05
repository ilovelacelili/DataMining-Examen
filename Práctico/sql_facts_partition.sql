CREATE TABLE fact_usage (
    usage_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    plan_id INT NOT NULL,
    usage_date DATE NOT NULL,
    service_type VARCHAR(50) NOT NULL,
    usage_amount FLOAT NOT NULL,
    revenue FLOAT NOT NULL
) PARTITION BY RANGE (usage_date);

CREATE TABLE fact_usage_jan_2025 PARTITION OF fact_usage
    FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE fact_usage_feb_2025 PARTITION OF fact_usage
    FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');