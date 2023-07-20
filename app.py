from views.cli_view import ViewCLI
from controllers import controller
from models import complex_number


view = ViewCLI()
model = complex_number.ComplexNumber
controller = controller.Controller(view, model)
controller.run()
