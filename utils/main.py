from metaapi_cloud_sdk import MetaStats, MetaApi
import asyncio
import os


async def example():
    # your MetaApi API token
    token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIyODQxMmYzMTYwN2Y4ZTEyOTc0NGM4MDkwNmRhMjQ4ZiIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MjhjOThjYzEtY2M2MS00MjIwLThhMzktZTQ4OTZhZDc0NmE1Il19LHsiaWQiOiJtZXRhYXBpLXJlc3QtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDoyOGM5OGNjMS1jYzYxLTQyMjAtOGEzOS1lNDg5NmFkNzQ2YTUiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjI4Yzk4Y2MxLWNjNjEtNDIyMC04YTM5LWU0ODk2YWQ3NDZhNSJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjI4Yzk4Y2MxLWNjNjEtNDIyMC04YTM5LWU0ODk2YWQ3NDZhNSJdfSx7ImlkIjoibWV0YXN0YXRzLWFwaSIsIm1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDoyOGM5OGNjMS1jYzYxLTQyMjAtOGEzOS1lNDg5NmFkNzQ2YTUiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MjhjOThjYzEtY2M2MS00MjIwLThhMzktZTQ4OTZhZDc0NmE1Il19XSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaW1wZXJzb25hdGVkIjpmYWxzZSwicmVhbFVzZXJJZCI6IjI4NDEyZjMxNjA3ZjhlMTI5NzQ0YzgwOTA2ZGEyNDhmIiwiaWF0IjoxNjkzNTA3NjAyLCJleHAiOjE3MDEyODM2MDJ9.mqS2L9QW7HzDzClG3aZWgklQ-f6npQTqnoYCfs0RBJKS2xl4c3ByRC2wK7EOvJkLOIc6yR1BbVdYhtfTY1ISUqNIsfHbYZjKgu0z6-6Hjyv-eC-nv_Zf7lN7a11bCOawzhENFe_wnmiYusHqevYpFLAZDdphdZs41n2nDxxhzU8I20CRMR-hOY_axJZoG_2AFmeK9RrNJLUedmyOWsqF0xJlotVpn3x4iESIeh9CO_C31B45OGs746VDMsaQkoEvZF2IfA_YvwERqtfs9WMWKo2P5dTn5IcdSP1M3MmBW2tPZgIWWRA7FFGpXWzXa9fy5kP8RBYSSrCaAdEBz8C0fJ38B-9sCaLoG8UBnJR6VDFnOOCEEHE_q0l9WPKV1Tn29Uzu3lZpse-0oOXNlNzUt0u_nEB4Q0wowG6Iy1nREgWbBoYMVFKNeK9WkE0sEuXPCllQL3D2tQt0T-UppvF557CVAjcI9A88VkruqGWXobITZf7gJ_aNoDf760vlfg3LeCZYwTwQ85DcHbzq1mpvGZoCDu1b7Z4Q28xolcKZDNdCfWK5BzgDZCmn_UH0-iHh7C9PUi1C7OjDAk-ZDSLt_0AYR-MVeTxcqT6J-SukGskt61qrhgxIuopF5iIwkez1jSY5g_BmVksRu2mXDupcX6fl8liUcQwFxI2rrOSakIk'
    # your MetaApi account id
    account_id = os.getenv('ACCOUNT_ID') or '28c98cc1-cc61-4220-8a39-e4896ad746a5'
    # your MetaApi account
    account = None

    api = MetaApi(token)
    meta_stats = MetaStats(token)
    # you can configure http client via second parameter,
    # see in-code documentation for full definition of possible configuration options

    async def account_deploy():
        try:
            nonlocal account
            account = await api.metatrader_account_api.get_account(account_id)

            #  wait until account is deployed and connected to broker
            print('Deploying account')
            if account.state != 'DEPLOYED':
                await account.deploy()
            else:
                print('Account already deployed')
            print('Waiting for API server to connect to broker (may take couple of minutes)')
            if account.connection_status != 'CONNECTED':
                await account.wait_connected()

        except Exception as err:
            print(meta_stats.format_error(err))

    await account_deploy()

    async def get_account_metrics():
        try:
            metrics = await meta_stats.get_metrics(account_id)
            print(metrics)  # -> {'trades': ..., 'balance': ..., ...}
        except Exception as err:
            print(meta_stats.format_error(err))

    await get_account_metrics()

    async def get_account_trades(start_time, end_time):
        try:
            trades = await meta_stats.get_account_trades(account_id, start_time, end_time)
            print(trades[-5:])  # -> {_id: ..., gain: ..., ...}
        except Exception as err:
            print(meta_stats.format_error(err))

    await get_account_trades('2023-08-31 00:00:00.000', '2023-08-31 00:09:00.000')

    async def get_account_open_trades():
        try:
            trades = await meta_stats.get_account_open_trades(account_id)
            print(trades)  # -> {_id: ..., gain: ..., ...}
        except Exception as err:
            print(meta_stats.format_error(err))

    await get_account_open_trades()

asyncio.run(example())
