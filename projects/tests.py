from django.test import TestCase

# Create your tests here.


if innovation_ratio > 5:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation++")  
    elif 0 < innovation_ratio <= 5:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation+") 
    elif -5 <= innovation_ratio < 0:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation-")
    elif innovation_ratio < -5:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation--")    
    else:
        statement_2 = get_object_or_404(GamificationAdvice, name="innovation0")