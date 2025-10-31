import os
from langchain.agents import create_agent

# from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

# from langchain.schema import SystemMessage
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()


class CustomerServiceTools:
    @staticmethod
    @tool(
        description="Get details of an order by order ID.",
        name_or_callable="get_order_details",
    )
    def get_order_details(order_id: str) -> str:
        try:
            # Simulate fetching order details from a database
            # [TODO]: Replace with actual database/API call
            order_database = {
                "123": "Order 123: Widget A, Quantity: 2, Status: Shipped",
                "456": "Order 456: Widget B, Quantity: 1, Status: Processing",
                "789": "Order 789: Widget C, Quantity: 5, Status: Delivered",
            }
            order = order_database.get(order_id, "Order not found.")
            return f"Order {order_id}: {order.get('status', 'not found')}. Tracking: {order.get('tracking', 'N/A')}"

        except Exception as e:
            return f"Error retrieving order details: {str(e)}"

    @staticmethod
    @tool(
        name_or_callable="get_shipping_status",
        description="Get shipping status by tracking number.",
    )
    def get_shigpping_status(tracking_number: str) -> str:
        try:
            # Simulate fetching shipping status from a shipping API
            # [TODO]: Replace with actual API call
            shipping_status_database = {
                "UPS-1Z999999": "Shipped via UPS, Tracking Number: 1Z999AA10123456784",
                "FEDEX-123456": "Delivered - Signed by: Reception",
                "OJ967902094GB": "Processing, not yet shipped.",
                "YZ967903456GB": "Delivered on 2025-09-15",
            }
            return shipping_status_database.get(
                tracking_number, "Shipping status not found."
            )

        except Exception as e:
            return f"Error retrieving shipping status: {str(e)}"

    @staticmethod
    @tool(
        name_or_callable="generate_coupon_code",
        description="Generate a coupon code for a customer given their email and discount percentage.",
    )
    def generate_coupon_code(customer_email: str, discoount: int) -> str:
        coupon_code = f"DISCOUNT{discoount}_{customer_email.split('@')[0].upper()}"
        return f"Generated coupon code: {coupon_code} for {discoount}% off."


def setup_customer_service_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )

    # tools = [
    #     Tool(
    #         func=CustomerServiceTools.get_order_details,
    #         name="get_order_details",
    #         description="Get details of an order by order ID.",
    #     ),
    #     Tool(
    #         func=CustomerServiceTools.get_shigpping_status,
    #         name="get_shipping_status",
    #         description="Get shipping status by tracking number.",
    #     ),
    #     Tool(
    #         func=CustomerServiceTools.generate_coupon_code,
    #         name="generate_coupon_code",
    #         description="Generate a coupon code for a customer given their email and discount percentage.",
    #     ),
    # ]

    tools = [
        CustomerServiceTools.get_order_details,
        CustomerServiceTools.get_shigpping_status,
        CustomerServiceTools.generate_coupon_code,
    ]
    system_message = """You are a professional customer service agent. 
            Be helpful, empathetic, and accurate. 
            Always verify order details before providing information.
            For shipping delays, offer a coupon as compensation.
            """

    # agent = initialize_agent(
    #     tools,
    #     llm,
    #     agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True,
    #     agent_kwargs={
    #         "system_message": system_message,
    #     },
    # )

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_message,
    )

    return agent


def main():
    agent = setup_customer_service_agent()
    queries = [
        "Can you provide the details for order ID 123?",
        "What's the shipping status for tracking number UPS-1Z999999?",
        "My order is delayed, can you help?",
    ]

    for query in queries:
        print(f"n{'=' * 50}")
        print(f"User Query: {query}")
        print(f"{'=' * 50}")
        try:
            response = agent.invoke(
                {"messages": [{"role": "user", "content": query}]},
            )
            print(f"Agent Response: {response}")
        except Exception as e:
            print(f"Error during agent execution: {str(e)}")


if __name__ == "__main__":
    main()
