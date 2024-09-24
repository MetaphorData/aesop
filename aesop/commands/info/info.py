import csv
import sys

import rich
import rich.table

from aesop.commands.common.enums.output_format import OutputFormat
from aesop.commands.common.exception_handler import exception_handler
from aesop.config import AesopConfig
from aesop.console import console


@exception_handler(command="info")
def info(
    output: OutputFormat,
    config: AesopConfig,
) -> None:
    setup_info = config.get_graphql_client().get_setup_info().setup_info

    if output is OutputFormat.JSON:
        console.print(setup_info.model_dump())
    else:
        header = ["Service", "Key", "Value"]
        oidc_rows = [
            ["OIDC", "Sign-in redirect URL", setup_info.oidc.sign_in_redirect_url],
        ]
        saml_rows = [
            ["SAML", "Entity ID", setup_info.saml.entity_id],
            ["SAML", "Reply ACS URL", setup_info.saml.reply_acs_url],
            ["SAML", "Sign-on URL", setup_info.saml.sign_on_url],
        ]
        crawler_ip_rows = [
            ["CRAWLER", "IP Address", value]
            for value in setup_info.crawler_ip_addresses
        ]
        if output is OutputFormat.CSV:
            spamwriter = csv.writer(sys.stdout)
            spamwriter.writerow(header)
            rows = oidc_rows + saml_rows + crawler_ip_rows
            spamwriter.writerows(rows)
        else:
            table = rich.table.Table(title="Metaphor Setup Info")
            for i, column in enumerate(header):
                table.add_column(
                    column, style="bold cyan" if i == 0 else None, no_wrap=True
                )
            for rows in [oidc_rows, saml_rows, crawler_ip_rows]:
                last_key = ""
                for i, row in enumerate(rows):
                    service = row[0] if i == 0 else None
                    key = None if last_key == row[1] else row[1]
                    last_key = row[1] if last_key != row[1] else last_key
                    table.add_row(
                        service, key, row[2], end_section=(i == len(rows) - 1)
                    )
            console.print(table)
