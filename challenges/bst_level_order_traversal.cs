public IList<IList<int>> LevelOrder(TreeNode root) 
{
    IList<IList<int>> nodes = new List<IList<int>>();
    if (root == null) return nodes;
    
    var queue = new Queue<KeyValuePair<TreeNode, int>>();
    queue.Enqueue(new KeyValuePair<TreeNode, int>(root, 0));
    
    while (queue.Count > 0)
    {
        var kvp = queue.Dequeue();
        var node = kvp.Key;
        int level = kvp.Value;
        
        if (level >= nodes.Count) nodes.Add(new List<int>());
        nodes[level].Add(node.val);
        
        if (node.left != null) queue.Enqueue(new KeyValuePair<TreeNode, int>(node.left, level + 1));
        if (node.right != null) queue.Enqueue(new KeyValuePair<TreeNode, int>(node.right, level + 1));
    }
    return nodes;
}
