class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
        if not self.root:
            return None
        
        queue = [self.root]
        
        while queue:
            current_node = queue.pop(0)
            
            if current_node.get('id') == id:
                return current_node
            
            queue.extend(current_node.get('children', []))
        
        return None

  # def get_element_by_id(self, id):
  #     return self._get_element_by_id_recursive(self.root, id)
    
  # def _get_element_by_id_recursive(self, node, id):
  #     # Base case: if the current node is None, return None
  #     if node is None:
  #         return None
      
  #     # Check if the current node's id matches the target id
  #     if node.get('id') == id:
  #         return node
      
  #     # Recursively search in the children nodes
  #     for child in node.get('children', []):
  #         result = self._get_element_by_id_recursive(child, id)
  #         if result is not None:
  #             return result
      
  #     # If the element is not found in the current node or its children, return None
  #     return None

        