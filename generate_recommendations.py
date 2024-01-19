import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load user data
user_data = pd.read_csv('user_data.csv')

# Load service data
service_data = pd.read_csv('service_data.csv')

# Merge user and service data
merged_data = pd.merge(user_data, service_data, on='service_id')

# Create user-service matrix
user_service_matrix = merged_data.pivot_table(index='user_id', columns='service_id', values='rating')

# Calculate similarity between users
user_similarity = cosine_similarity(user_service_matrix)

# Function to generate recommendations for a user
def generate_recommendations(user_id, top_n=5):
    # Get index of the user
    user_index = user_service_matrix.index.get_loc(user_id)
    
    # Calculate similarity scores with other users
    similarity_scores = user_similarity[user_index]
    
    # Get top similar users
    top_similar_users = similarity_scores.argsort()[:-top_n-1:-1]
    
    # Get services rated by similar users
    services_rated_by_similar_users = user_service_matrix.iloc[top_similar_users].dropna(axis=1)
    
    # Calculate average rating for each service
    service_avg_ratings = services_rated_by_similar_users.mean()
    
    # Sort services based on average ratings
    recommended_services = service_avg_ratings.sort_values(ascending=False)[:top_n]
    
    return recommended_services

# Generate recommendations for a user
user_id = 1
recommendations = generate_recommendations(user_id, top_n=5)

# Print sample recommendation output
print(f"Recommendations for User {user_id}:")
for i, (service_id, rating) in enumerate(recommendations.iteritems(), 1):
    print(f"{i}. Service ID: {service_id}, Rating: {rating}")
