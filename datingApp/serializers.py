'''
class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    def validate_email(self, email):
    """
    Verify that the mailbox is legal
    """
    # Whether the mailbox is registered
    if User.objects.filter(email = email).count():
    raise serializers.ValidationError(' This email has been registered ')
    # Verify that the email number is legal
    if not re.match(EMAIL_REGEX, email):
    raise serializers.ValidationError(' Mailbox format error ')
    # Verification code sending frequency
    one_minute_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
    if VerifyCode.objects.filter(add_time__gt=one_minute_age, email=email).count():
    raise serializers.ValidationError(' Please send again in a minute ')
    return email
'''