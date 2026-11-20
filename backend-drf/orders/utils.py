# from django.core.mail import send_mail
# from django.conf import settings



# def send_order_notification(order):
#     send_mail(
#         subject=f'Order #{order.id} is received',
#         message=f"""
#             Hi {order.user.first_name},

#             Your order #{order.id} has been placed successfully.

#             Total: {order.grand_total}

#             Thank you for shopping with us.
#         """,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[order.user.email],
#         fail_silently=False
#     )

import resend
from django.conf import settings


def send_order_notification(order):

    # Configure Resend API key
    resend.api_key = settings.RESEND_API_KEY

    # Send order confirmation email
    params = {
        "from": "ClickMart <onboarding@resend.dev>",
        "to": [order.user.email],
        "subject": f"Order #{order.id} is received",
        "html": f"""
            <h2>Hi {order.user.first_name},</h2>

            <p>Your order <strong>#{order.id}</strong>
            has been placed successfully!</p>

            <p><strong>Total:</strong> {order.grand_total}</p>

            <p>Thank you for shopping with ClickMart!</p>
        """,
    }

    email = resend.Emails.send(params)

    print(f"Resend email sent successfully: {email}")

    return email
