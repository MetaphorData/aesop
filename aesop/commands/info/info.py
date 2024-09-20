import csv
import sys
from wsgiref import headers
import rich
import rich.table
import typer
from aesop.console import console
from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.graphql.generated.custom_fields import OIDCFields, SAMLFields, SetupInfoFields
from aesop.graphql.generated.custom_queries import Query


@exception_handler(command="info", exception_type=Exception)
def info(
    output: OutputFormat,
    config: AesopConfig,
) -> None:
    setup_info_query = Query.setup_info().fields(
        SetupInfoFields.oidc().fields(OIDCFields.signInRedirectUrl),
        SetupInfoFields.saml().fields(
            SAMLFields.entityId, SAMLFields.replyACSUrl, SAMLFields.signOnUrl
        ),
        SetupInfoFields.crawlerIpAddresses,
    )
    res = config.get_graphql_client().query(setup_info_query, operation_name="getInfo")
    setup_info = res["setupInfo"]

    if output is OutputFormat.JSON:
        console.print(setup_info)
    else:
        header = ["Service", "Key", "Value"]
        oidc_rows = [
            ["OIDC", "Sign-in redirect URL", setup_info["oidc"]["signInRedirectUrl"]],
        ]
        saml_rows = [
            ["SAML", "Entity ID", setup_info["saml"]["entityId"]],
            ["SAML", "Reply ACS URL", setup_info["saml"]["replyACSUrl"]],
            ["SAML", "Sign-on URL", setup_info["saml"]["signOnUrl"]],
        ]
        crawler_ip_rows = [
            ["CRAWLER", "IP Address", value]
            for value in setup_info["crawlerIpAddresses"]
        ]
        if output is OutputFormat.CSV:
            spamwriter = csv.writer(sys.stdout)
            spamwriter.writerow(header)
            rows = oidc_rows + saml_rows + crawler_ip_rows
            spamwriter.writerows(rows)
        else:
            table = rich.table.Table(title="Metaphor Setup Info")
            for i, column in enumerate(header):
                table.add_column(column, style="bold cyan" if i == 0 else None, no_wrap=True)
            for rows in [oidc_rows, saml_rows, crawler_ip_rows]:
                last_key = ""
                for i, row in enumerate(rows):
                    service = row[0] if i == 0 else None
                    key = None if last_key == row[1] else row[1]
                    last_key = row[1] if last_key != row[1] else last_key
                    table.add_row(service, key, row[2], end_section=(i == len(rows) - 1))
            console.print(table)
                
