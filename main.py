from markupsafe import Markup

def define_env(env):
    @env.macro
    def recipe(inputs, output):
        def slot(item):
            if not item:
                return '<span class="invslot"></span>'
            return (
                '<span class="invslot">'
                    '<span class="invslot-item"><span>'
                        f'<a target="_blank" href="{item["link"]}">'
                            f'<img title="{item["name"]}" src="{item["icon"]}" width="32" height="32">'
                        '</a>'
                    '</span></span>'
                '</span>'
            )

        rows = ['<span class="mcui-row">' + ''.join(slot(x) for x in row) + '</span>' for row in inputs]

        count_html = f'<span class="invslot-stacksize">{output["count"]}</span>' if "count" in output else ''
        output_html = (
            '<span class="invslot invslot-large"><span class="invslot-item"><span>'
                f'<a href="{output["link"]}">'
                    f'<img title="{output["name"]}" src="{output["icon"]}" width="32" height="32">'
                '</a>'
            f'</span><a href="{output["link"]}">{count_html}</a></span></span>'
        )

        # 关键点：整串 HTML 从第一个字符就开始，不要任何前导换行和空格
        html = (
            '<div>'
                '<span class="mcui mcui-Crafting_Table">'
                    '<span class="mcui-input">' + ''.join(rows) + '</span>'
                    '<span class="mcui-arrow"><br></span>'
                    '<span class="mcui-output">' + output_html + '</span>'
                '</span>'
            '</div>'
        )
        return Markup(html)  # 标记为“安全 HTML”
