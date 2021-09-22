import ast
import inspect
import typing as typ
from DevAuto.lang_imp import DFunc, Inst


class Translator:

    def trans(self, func: DFunc) -> typ.List[Inst]:
        """
        Transform a DFunc into list of Insts.
        """
        pyfunc = func.body()

        # Transform AST nodes
        ast_nodes = ast.parse(inspect.getsource(pyfunc))
        DA_NodeTransformer().visit(ast_nodes)

        # Append a call expr
        # without this expr the pyfunc will not be executed
        # in exec()
        expr = ast.Expr(
            ast.Call(
                func = ast.Name(id=pyfunc.__name__, ctx=ast.Load()),
                args = [],
                keywords = []))
        ast_nodes.body.append(expr)

        # Transform from ast to List[Inst]
        target_insts = []
        global_env, loc_env = {}, { "insts": target_insts }
        exec(compile(ast_nodes, "", 'exec'),
             global_env,
             loc_env)

        return target_insts


class DA_NodeTransformer(ast.NodeTransformer):
    """
    Transform a DFunc into intermidiate form which able
    to be execute by python interpreter to generate a list
    of DA instructions.
    """

    def __init__(self) -> None:
        self._precheck_transformer = DA_NodeTransPreCheck()
        self._trans_transformer = DA_NodeTransTransform()

    def visit(self, node: ast.AST) -> None:
        """
        Make transformations to DFunc's ast nodes
        """

        # Make sure the ast is able to be transformed
        self._precheck_transformer.visit(node)

        # Do Transformation
        self._trans_transformer.visit(node)


class DA_NodeTransPreCheck(ast.NodeTransformer):
    """
    Do prechecking to ast nodes of DFunc
    """

    def visit_Expr(self, ) -> None:
        """
        Transform into components of DA into intermidate form.
        """


class DA_NodeTransTransform(ast.NodeTransformer):
    """
    Do transfromations to ast nodes of DFunc
    """
