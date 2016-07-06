# import yaml

class Generator:
    def __init__(self):
         self.data = None

    def generate(self):
        # with open(path, 'r') as source:
        #     self.data = yaml.load(source.read())
        # source.close()
        # print(self.data)
        str_list_products = []

        str_list_products.append('<openerp>\n\t<data>')

        for i in xrange(1, 2000):
            str_list_products.append('\n\t\t<record id="object{0}" model="pagination.pagination">'
                                    '\n\t\t\t<field name="name">Object {0}</field>\n\t\t</record>'.format(i))

        str_list_products.append('\n\t</data>\n</openerp>')

        products = ''.join(str_list_products)
        # print products

        file_demo = file('../demo.xml', 'w')
        for index in products:
            file_demo.write(index)

if __name__ == '__main__':
    generator = Generator()
    generator.generate()

            # <openerp>
            #         <data>
            #             <record id="object0" model="pagination.pagination">
            #                     <field name="name">Object 0</field>
            #             </record>
            #         </data>
            # </openerp>